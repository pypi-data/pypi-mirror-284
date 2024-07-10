import numpy as np
import os
import copy
from .helper_func import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import pickle
from bisect import bisect

class GacaFieldData:
    '''
    Class to create a field data file (\*_gaca.fd.txt) as input for TSWC-GACA.
    Later on the following methods need to be performed for each instance of the class.
    For each step the according methods will check for correct inputs and prevent error in the exported txt-file.

    Workflow for Generating field data.

    ---- 1. BOREHOLE ----
        1. 'add_boreholeVector'
        2. 'add_radialComment' (optional)
        3. 'add_boreholeInclination'
        4. 'add_materialProperty' (depending on vertical discretisation)
        5. 'add_temperature' - borehole
    ---- 2. CAVNERN ----
        1. 'add_cavernVector'
        2. 'add_temperature' - cavern
        3. 'add_cavernCharacteristics'

    ---- The last step is to export the field data to an txt-file with the method 'export_fieldData'. ----
    '''

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    def __init__(self,n_boreholes:int, n_fluid:int, tvd:float, delta_z:float,
                 medium_type_cavern:str,medium_id_cavern:str):
        """Initialise GacaFieldData class.

        :param n_boreholes:  usually 1
        :type n_boreholes: int
        :param n_fluid: how many flow spaces (Strömungsräume)
        :type n_fluid: int
        :param tvd: maximum TVD of the borehole
        :type tvd: float
        :param delta_z: vertical discretisation of TVD_max
        :type delta_z: float
        :param medium_type_cavern: Which medium type (must be 'GAS')
        :type medium_type_cavern: str
        :param medium_id_cavern: which substance (defined in fluid library of TSWC)
        :type medium_id_cavern: str
        """        
        self.n_boreholes        = n_boreholes   
        self.n_fluid            = n_fluid
        self.p_borehole         = int(np.round(tvd / delta_z))
        self.delta_z    	    = delta_z
        self.medium_type_cavern = medium_type_cavern
        self.medium_id_cavern   = medium_id_cavern

        self.m_borehole         = -1   # specified later, -1 for assertation purpose
        self.m_cavern           = -1
        self.tvd   = tvd
        self.radialComment      = None


        self.materialNames = [''] * self.p_borehole

        self.radial_vector_borehole    = [] 
        self.heat_capacity             = None
        self.thermal_conductivity      = None
        self.bottom_edge_vertical = np.linspace(start=0, stop=self.tvd, num = self.p_borehole + 1)[1:]

    def add_boreholeVector(self,radial_vector, aggregate_state): #TODO: Unit conversion
        """Adds a radial vector within the borehole [m] and respective aggregate states ('FLUID' or 'SOLID').

        :param radial_vector: must be strictly increasing, will define self.m_borehole [int].
        :type radial_vector:  list or array [m] 
        :param aggregate_state: list of strings either 'FLUID' or 'SOLID'.
                                Does not need to have the same length as radial_vector.
                                Remaining values will be filled with 'SOLID'.
        :type aggregate_state: string array
        """      

        assert all(i < j for i, j in zip(radial_vector, radial_vector[1:])), 'List is not strictly increasing!'
        self.radial_vector_borehole    = radial_vector
        self.m_borehole                = radial_vector.shape[0]

        # Create vector for aggregate states (column_character_borehole), check spelling
        column_character_borehole = []
        for element in aggregate_state:
            state = element.upper()
            assert state in ['FLUID', 'SOLID'], 'Rechtschreibfehler in column_character_borehole %s' %(element)
            column_character_borehole.append(state)

        assert column_character_borehole.count('FLUID') == self.n_fluid, '"FLUID" does not match self.n_fluid!'
        
        diff = self.m_borehole - len(column_character_borehole) 
        if diff > 0 : # Fill remaining values with 'SOLID' so user only needs to define states near construction (formation points are always solid)
        
            for _ in range(diff):
                column_character_borehole.append('SOLID')
            
        self.column_character_borehole = column_character_borehole

        # pre-allocate space for material properties
        self.thermal_conductivity = np.ones((self.p_borehole, self.m_borehole))*-1 
        self.heat_capacity        = np.ones((self.p_borehole, self.m_borehole))*-1 
       

    def add_radialComment(self,radialComment):
        """Add comments for radial borehole vector. Will be displayed lather in txt file (OPTIONAL - for overview purpose only).
        If the array has a length of e.g. 5, then the comment is valid for the first five radial elements.
        

        :param radialComment: E.g. ['ID 858','OD 858','ID 1134', 'ZEMENT', 'FORMATION']
        :type radialComment: array
        """      
        self.radialComment = radialComment

    def add_cavernVector(self,radial_vector): 
        """Adds a radial vector within the cavern. The first element is the cavern radius.

        :param radial_vector: must be strictly increasing, will define self.m_cavern [int].
        :type radial_vector: list or array [m]
        """      
        assert all(i < j for i, j in zip(radial_vector, radial_vector[1:])), 'List is not strictly increasing!'

        self.radial_vector_cavern = radial_vector
        self.m_cavern = radial_vector.shape[0]

    def add_boreholeInclination(self,inclination):
        """Add inclination for borehole

        :param inclination: either array [1 x p_borehole] with deg data or 'vertical'
        :type inclination: array [1xp_borehole] oder 'vertical'
        """        
        if type(inclination) == str: 
            self.inclination = np.zeros([self.p_borehole,1])
        else:
            self.inclination = inclination

    
    def add_materialProperty(self,top,bottom,heat_capacity,thermal_conductivity,name=None):
        """Adds material properties to the borehole.
        The value for the center of gravity of the layer is then modeled, with indication in relation to the bottom edge of the layer. 
        Hierarchical; new values overwrite respective old values at the same intervals.

        :param top: start of layer [m]
        :type top: int or float
        :param bottom: end of layer [m]
        :type bottom: int or float
        :param heat_capacity:  [MJ/(m3K)]
        :type heat_capacity: array [1 x m_borehole]
        :param thermal_conductivity: [1 x m_borehole] 
        :type thermal_conductivity: [W/(m K)]
        :param name:  Name of the layer, will be displayed in .txt file when exported, defaults to None
        :type name: str, optional
        """        
        assert self.m_borehole > 0, 'Please define radial_vector_borehole via add_boreholeVector first.'
        assert heat_capacity.shape[0] == self.m_borehole, 'Fehler bei cp in %s' %(name)
        assert thermal_conductivity.shape[0] == self.m_borehole, 'Fehler bei T in %s' %(name)

        idx_top     = find_nearest(self.bottom_edge_vertical,top)
        idx_bottom  = find_nearest(self.bottom_edge_vertical,bottom)

        self.heat_capacity[idx_top:idx_bottom + 1,:]        = heat_capacity
        self.thermal_conductivity[idx_top:idx_bottom + 1,:] = thermal_conductivity

        if name is not None:
            for i in range(idx_top, idx_bottom + 1):
                self.materialNames[i] = name

    def initialise_formation(self, radial_vector_formation):
        """Initilise radial points for formation

        :param radial_vector_formation: radial points
        :type radial_vector_formation: array
        """
        if all(i < j for i, j in zip(radial_vector_formation, radial_vector_formation[1:])) == False:
            print('radial_vector is not strictly increasing, it will be sorted')
            radial_vector_formation = np.sort(radial_vector_formation)

        self.m_borehole = radial_vector_formation.shape[0]
        self.thermal_conductivity = np.zeros((self.p_borehole, self.m_borehole))
        self.heat_capacity        = np.zeros((self.p_borehole, self.m_borehole))
        self.radial_vector_borehole = radial_vector_formation

    def add_formation(self, top, bottom, heat_capacity_val, thermal_conductivity_val, name:str = None):
        """Add Formation elements after having initilised formation.

        :param top: start of layer [m]
        :type top: int or float
        :param bottom: end of layer [m]
        :type bottom: int or float
        :param heat_capacity_val:  [MJ/(m3K)]
        :type heat_capacity_val: int or float
        :param thermal_conductivity_val: [W/(m K)]
        :type thermal_conductivity_val: int or float
        :param name: Name of the layer, will be displayed in .txt file when exported, defaults to None, defaults to None
        :type name: str, optional
        """
        idx_top     = find_nearest(self.bottom_edge_vertical,top)
        idx_bottom  = find_nearest(self.bottom_edge_vertical,bottom)

        self.heat_capacity[idx_top:idx_bottom + 1,:]        = heat_capacity_val
        self.thermal_conductivity[idx_top:idx_bottom + 1,:] = thermal_conductivity_val

        if name is not None:
            for i in range(idx_top, idx_bottom + 1):
                self.materialNames[i] = name

    def add_element(self, starting_coor:tuple, end_coor:tuple, heat_capacity_val:float,
                    thermal_conductivity_val:float, name = None):
        """Add material properties of an element to the borehole model. 

        :param starting_coor: (z0, x0) - Top coordinates of element at the top left corner.
        :type starting_coor: tuple
        :param end_coor: (z1, x1) - Bottom coordinates of element at the bottom right corner.
        :type end_coor: tuple
        :param heat_capacity_val: [MJ/(m3K)]
        :type heat_capacity_val: float
        :param thermal_conductivity_val: _description_
        :type thermal_conductivity_val: [W/(m K)]
        :param name: Name, defaults to None
        :type name: _type_, optional
        """
        radial_vector_borehole = self.radial_vector_borehole
        thermal_conductivity   = self.thermal_conductivity
        heat_capacity          = self.heat_capacity

        # check if matrices have been initilized
        if np.any([heat_capacity is None, thermal_conductivity is None]):
            print('Please initilise the geological formation with the function initialise_formation() and add values to it with add_formation().')
            return
        
        # check all points have non-zero values in matrices
        if np.any([np.nonzero(heat_capacity == 0), np.nonzero(thermal_conductivity == 0)]):
            print('There are still zero values in the matrices heat_capacity or thermal_conductivity. Please check that all points have been allocated with values.')
            return

        x0 = starting_coor[1]
        x1 = end_coor[1]
        z0 = starting_coor[0]
        z1 = end_coor[0]  

        z_i0 = find_nearest(self.bottom_edge_vertical, z0)
        z_i1 = find_nearest(self.bottom_edge_vertical, z1) + 1  # +1 due to slicing principle in python

        i_x_new = []
        for x_val in [x0, x1]:
            if x_val not in radial_vector_borehole: 
                i_new_temp = bisect(radial_vector_borehole, x_val)
                radial_vector_borehole = np.insert(radial_vector_borehole, i_new_temp, x_val) # add new x_val to radial borehole vector
                print('Inserted new radial point at %.4fm' % (x_val))
                if i_new_temp == thermal_conductivity.shape[1]:
                    new_col_therm = thermal_conductivity[:, -1]
                else:
                    new_col_therm = thermal_conductivity[:, i_new_temp]
                thermal_conductivity = np.insert(thermal_conductivity, i_new_temp, new_col_therm, axis = 1)

                if i_new_temp == heat_capacity.shape[1]:
                    new_col_heat = heat_capacity[:, -1]
                else:
                    new_col_heat = heat_capacity[:, i_new_temp]
                heat_capacity = np.insert(heat_capacity, i_new_temp, new_col_heat, axis = 1)

                i_x_new.append(i_new_temp)
            else:
                i_x_new.append(find_nearest(radial_vector_borehole, x_val))

        thermal_conductivity[z_i0:z_i1, i_x_new[0] + 1:i_x_new[1] + 1] = thermal_conductivity_val
        heat_capacity[z_i0:z_i1, i_x_new[0] + 1:i_x_new[1] + 1]        = heat_capacity_val
        
        print('Updated values for points:')
        for z_val in self.bottom_edge_vertical[z_i0:z_i1]:
            print('- %.2f m |  ' %(z_val), end ='')
            for x_val in radial_vector_borehole[i_x_new[0] + 1:i_x_new[1] + 1]:
                print('%.3f m \t' %(x_val) , end = '')
            print('| c*rho = %.2f MJ/(K*m3) | lambda = %.2f W/(m*K)\n' %(heat_capacity_val, thermal_conductivity_val), end = "")

        if name is not None:
            for i in range(z_i0, z_i1):
                self.materialNames[i] += '_' + name

        self.thermal_conductivity      = thermal_conductivity
        self.heat_capacity             = heat_capacity
        self.radial_vector_borehole    = radial_vector_borehole
        self.m_borehole                = radial_vector_borehole.shape[0]
        self.column_character_borehole = ['SOLID'] * self.m_borehole

    def define_fluid_space(self, indices, names):
        """Define which elements of radial_borehole_vector are not 'SOLID'-

        :param indices: If integer -> index, if float -> search for closest match in radial_borehole_vector
        :type indices: int or float
        :param names: either 'FLUID' or ???
        :type names: string
        """
        if type(indices) is not list: indices = [ indices ]
        if type(names) is not list: names = [ names ]

        assert len(indices) == len(names)
        for idx, name in zip(indices, names):
            assert name in ['FLUID', 'SOLID']
            if isinstance(idx, int):
                idx_temp = idx
            elif isinstance(idx, float):
                idx_temp = find_nearest(self.radial_vector_borehole, idx)
            else:
                print(f'Could not find any match for {idx}. Please check if it is either a int or float.')
                continue
            self.column_character_borehole[idx_temp] = name
            self.heat_capacity[:, idx_temp] = 0
            self.thermal_conductivity[:, idx_temp] = 0
            print('Set %.4f m as %s. Material properties for this element are set to 0.' %(self.radial_vector_borehole[idx_temp], name))


    def add_temperature(self, temperature, mode:str):
        """ Adds temperature data to the borehole or cavern.

        :param temperature: (p_borehole x m_borehole) array for 'borehole or
                        (m_cavern) for cavern 
        :type temperature: _type_
        :param mode: either 'borehole' or 'cavern'
        :type mode: str
        """    
        match mode:
            case 'borehole':
                assert self.m_borehole > 0, 'Please define radial_vector_borehole via add_boreholeVector first.'
                assert temperature.shape == (self.p_borehole, self.m_borehole)
                self.temperature_borehole = temperature

            case 'cavern':
                assert self.m_cavern > 0, 'Please define radial_vector_cavern via add_boreholeVector first.'
                assert temperature.shape == (self.m_cavern,)
                self.temperature_cavern = temperature

        print('Added Temperature')

    def add_cavernCharacteristics(self,refdepth_cavern:float,density_salt:float,specific_heat_capacity_salt:float,heat_conductivity_salt:float,
                                  height_cavern:float, volume_brine_equivalent:float, radius_brine_level:float, pressure_cavern:float, temperature_brine_equivalent:float = None):
        """Add cavern characteristics:

        :param refdepth_cavern: reference depth for cavern pressure and modeling [m]
        :type refdepth_cavern: float
        :param density_salt:  [kg/m3]
        :type density_salt: float
        :param specific_heat_capacity_salt: [J/kgK]
        :type specific_heat_capacity_salt: float
        :param heat_conductivity_salt: [W/mK]
        :type heat_conductivity_salt: float
        :param height_cavern: consists of H_zy + 2*rad_cav [m]
        :type height_cavern: float
        :param volume_brine_equivalent: [m3]
        :type volume_brine_equivalent: float
        :param radius_brine_level: [m]
        :type radius_brine_level: float
        :param pressure_cavern: [MPa]
        :type pressure_cavern: float
        :param temperature_brine_equivalent: [°C], defaults to None
        :type temperature_brine_equivalent: float, optional
        """

        self.refdepth_cavern              = refdepth_cavern  
        self.density_salt                 = density_salt
        self.specific_heat_capacity_salt  = specific_heat_capacity_salt
        self.heat_conductivity_salt       = heat_conductivity_salt
        self.height_cavern                = height_cavern
        self.volume_brine_equivalent      = volume_brine_equivalent
        self.radius_brine_level           = radius_brine_level      
        self.temperature_brine_equivalent = temperature_brine_equivalent
        self.pressure_cavern              = pressure_cavern

    def plot_geometry(self, xlimits:list = None, export_folder:str = None):
        """Plots geometry.

        :param xlimits: start and end value of radial range, defaults to None
        :type xlimits: list, optional
        :param export_folder: Export plot data into folder, defaults to None
        :type export_folder: str, optional
        :return: Two figures for heat capacity * rho and lambda
        :rtype: fig_cp, fig_lambda
        """

        x = self.radial_vector_borehole
        y = self.bottom_edge_vertical  
        X,Y = np.meshgrid(np.insert(x, 0, 0), np.insert(y, 0, 0))

        colormap = mpl.colormaps.get_cmap('jet')
        colormap.set_bad('magenta')
        # heat capacity * rho
        fig_cp, ax = plt.subplots()
        fig_cp.canvas.manager.set_window_title('Geometry_HeatCapactiyRho') 
        Z = self.heat_capacity

        cm = ax.pcolormesh(X, Y, Z, cmap = colormap)
        
        ax.set_title('Dichte * spez. Wärmekapazität')
        plt.suptitle('Borehole geometry')
        ax.set_xlabel('x [m] (Beginned ab Bohrlochachse)')
        ax.set_ylabel('z [m]')
        ax.invert_yaxis()

        if xlimits is not None:
            ax.set(xlim=xlimits)

        cbar = plt.colorbar(cm, ax = ax) #, format = '%.1f K', label = 'Temperature')
        cbar.ax.set_title('[MJ/(K*m3)]', loc='center')
        # mplcursors.cursor(hover=2)
        # thermal conductivity
        fig_lambda, ax = plt.subplots()
        fig_lambda.canvas.manager.set_window_title('Geometry_ThermalConductivity') 
        Z = self.thermal_conductivity
        cm = ax.pcolormesh(X, Y, Z, cmap = colormap, vmax = 10)
        ax.set_title('Wärmeleitfähigkeit')
        plt.suptitle('Borehole geometry')
        ax.set_xlabel('x [m] (Beginned ab Bohrlochachse)')
        ax.set_ylabel('z [m]')
        ax.invert_yaxis()
        if xlimits is not None:
            ax.set(xlim=xlimits)
        cbar = plt.colorbar(cm, ax = ax) #, format = '%.1f K', label = 'Temperature')
        cbar.ax.set_title('[W/(m*K)]', loc='center')

        if export_folder is not None:
            if Path(export_folder).exists() and Path(export_folder).is_dir(): # it must be a valid path and a folder
                width  = 406 / 25.4 # inches
                height = 229 / 25.4 # inches
                dpi    = max([1536/width, 864/height])
                save_geom_path = Path(export_folder)

                fig_cp.set_size_inches(width, height)
                fig_cp.savefig(save_geom_path.joinpath('Geometry_HeatCapactiyRho.png'), dpi = dpi)
                print('Exported %s' %(save_geom_path.joinpath('Geometry_HeatCapactiyRho.png')))

                fig_lambda.set_size_inches(width, height)
                fig_lambda.savefig(save_geom_path.joinpath('Geometry_ThermalConductivity.png'), dpi = dpi)
                print('Exported %s' %(save_geom_path.joinpath('Geometry_ThermalConductivity.png')))   
            else:
                print('Für den Export bitte einen gültigen Ordnerpfad angeben.\n%s konnte nicht gefunden werden.\n' %(export_folder))

        return fig_cp, fig_lambda

    def export_fieldData(self,save_folder,project_name, is_binary_export:bool = False):
        """Exports class to a txt-File with the suffix "_gaca.fd.txt".
        Will be exported to a folder named (path, project_name). If it does not exist, it will be created.

        :param save_folder: path
        :type save_folder: str
        :param project_name: suffix on path, 
        :type project_name: str
        :param is_binary_export: Export class as a binary file (*.pickle). It can be later loaded to display to geometry for example in TSWC_TFBH.create_movie(), defaults to False
        :type is_binary_export: bool, optional
        """       
        save_path = os.path.join(save_folder, project_name)
        if not (os.path.exists(save_path)):
            os.makedirs(save_path)
            print('Created new folder %s' %(save_path))
        file_name = os.path.join(save_path ,project_name + '_gaca.fd.txt')
        fid = open(file_name, 'w')

        def write_npMatrix2Fid(matrix,axis=1,bottom_edges=None,fid=fid):

            if matrix.ndim > 1 or axis == 0:
                for i,row in enumerate(matrix):
                    row.tofile(fid,sep='\t',format='%.3f')
                    if bottom_edges is not None:
                        fid.write('\t# UK %.2fm - %s' %(bottom_edges[i], self.materialNames[i]))
                    fid.write('\n')    
            else:
                matrix.tofile(fid,sep='\t',format='%.4f')

        v_space   = '\n\n'

        fid.write('NUMBER_BOREHOLES\t%d\n' %(self.n_boreholes))																	
        fid.write('N_FLUID\t%d\n' %(self.n_fluid)	)														
        fid.write('M_BOREHOLE\t%d\t# (M)\n' %(self.m_borehole)	)														
        fid.write('P_BOREHOLE\t%d\t# (P)\n' %(self.p_borehole)	)															
        fid.write('DL\t%.4f\t# [m]\n' %(self.delta_z)	)													
        fid.write('M_CAVERN\t%d\t# (MK)\n' %(self.m_cavern)	)													
        fid.write('MEDIUM_TYPE_CAVERN\t%s\n' %(self.medium_type_cavern)	)																		
        fid.write('MEDIUM_ID_CAVERN\t%s\n' %(self.medium_id_cavern)	)	 						
        fid.write('DEPTH_CAVERN\t%.2f\t# Referenztiefe fuer Druck' %(self.refdepth_cavern)	)		
        fid.write(v_space)

        fid.write('RADIAL_VECTOR_BOREHOLE # [m]\n')
        if self.radialComment is not None:
            fid.write('#%s\n' %('\t'.join(self.radialComment)))		
        write_npMatrix2Fid(self.radial_vector_borehole)
        fid.write(v_space)

        fid.write('COLUMN_CHARACTER_BOREHOLE # [/] der Radialelemente um die Bohrung (M Werte)\n')	
        fid.write('\t'.join(self.column_character_borehole))
        fid.write(v_space)

        fid.write('HEAT_CAPACITY_BOREHOLE # [MJ/(K*m3)]  Dichte * spez. Waermekapazitaet der Radialelemente um die Bohrung (P*M Werte)\n')
        if self.radialComment is not None:
            fid.write('#%s\n' %('\t'.join(self.radialComment)))
        write_npMatrix2Fid(self.heat_capacity,bottom_edges=self.bottom_edge_vertical)
        fid.write(v_space)

        fid.write('THERMAL_CONDUCTIVITY_BOREHOLE # [W/(m*K)]  Waermeleitfaehigkeit der Radialelemente um die Bohrung (P*M Werte)\n')
        if self.radialComment is not None:
            fid.write('#%s\n' %('\t'.join(self.radialComment)))
        write_npMatrix2Fid(self.thermal_conductivity,bottom_edges=self.bottom_edge_vertical)
        fid.write(v_space)

        fid.write('TEMPERATURE_BOREHOLE  # [deg C] Temperatur der Radialelemente um die Bohrung (P*M Werte)\n')
        if self.radialComment is not None:
            fid.write('#%s\n' %('\t'.join(self.radialComment)))
        write_npMatrix2Fid(self.temperature_borehole,bottom_edges=self.bottom_edge_vertical)
        fid.write(v_space)

        fid.write('WELL_VERTICALITY  # [deg] Winkel zwischen Bohrlochachse und Bohrung (P Werte)\n')
        write_npMatrix2Fid(self.inclination,0,bottom_edges=self.bottom_edge_vertical)
        fid.write(v_space)

        fid.write('RADIAL_VECTOR_CAVERN # [m] (MK Werte)\n')
        write_npMatrix2Fid(self.radial_vector_cavern)
        fid.write(v_space)

        fid.write('TEMPERATURE_CAVERN  #  [deg C] Temperatur der Radialelemente um die Kaverne (MK Werte) \n')
        write_npMatrix2Fid(self.temperature_cavern)
        fid.write(v_space)

        fid.write('DENSITY_SALT\t%.2f\t#[kg/m3]\n' %(self.density_salt))																	
        fid.write('SPECIFIC_HEAT_CAPACITY_SALT\t%.2f\t#[J/(kg*K)]\n' %(self.specific_heat_capacity_salt))														
        fid.write('HEAT_CONDUCTIVITY_SALT\t%.2f\t#[W/(m*K)]\n' %(self.heat_conductivity_salt))														
        fid.write('HEIGHT_CAVERN\t%.2f\t#[m]\n' %(self.height_cavern))														
        fid.write('VOLUME_BRINE_EQUIVALENT\t%.2f\t#[m3]\n' %(self.volume_brine_equivalent))
        fid.write('RADIUS_BRINE_LEVEL\t%.2f\t#[m]\n' %(self.radius_brine_level))
        if self.temperature_brine_equivalent is not None:
            fid.write('TEMPERATURE_BRINE_EQUIVALENT\t%.2f\t#[deg C] optional\n' %(self.temperature_brine_equivalent))
        fid.write('PRESSURE_CAVERN\t%.2f\t#[MPa] at DEPTH_CAVERN %.2fm\n' %(self.pressure_cavern,self.refdepth_cavern))

        fid.close()
        print('Run sucessfull')
        print(file_name)

        if is_binary_export:
            save_path = os.path.join(save_path ,project_name + '_fd.pickle')
            with open(save_path, 'wb') as f:
                pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
                print('Exported %s\n' %(save_path))

####################################################################################


class GacaProcessData():
    def __init__(self,description, coupled_annuli, medium_type, medium_id):
        """Created process data for TSWC that can be exported to a txt-file.

        :param description: description to be displayed in txt-file.
        :type description: str
        :param coupled_annuli: _description_
        :type coupled_annuli: list or np.array [1 x N_FLUID]
        :param medium_type: _description_
        :type medium_type: string array [1 x N_FLUID]
        :param medium_id: _description_
        :type medium_id: list [1 x N_FLUID]
        """     
        assert len(coupled_annuli) == len(medium_id), 'MEDIUM ID und COUPLED ANNULI do must have same length!'
        self.description    = description
        self.medium_type    = medium_type
        self.medium_id      = medium_id
        self.coupled_annuli = coupled_annuli

        self.n_stages   = 0
        self.stages_param = dict()
        self.n_fluid = len(medium_type)

    def add_stage(self,stage_data: dict):
        """Erlaubt flexibles hinzufügen von stages. Stages werden chronologisch hinzugefügt.
        WICHTIG: Schlüsselnamen aus dict müssen mit Variablenname von TSWC übereinstimmen, erlaubt sind folgende Namen:
            - 'TERMINATION_ID',
            - 'TERMINATION_QUANTITY',
            - 'DT_MAX',
            - 'FLOW_RATE',
            - 'P_BOUNDARY_CONDITION',
            - 'BOUNDARY_PRESSURE',
            - 'T_BOUNDARY_CONDITION',
            - 'BOUNDARY_TEMPERATURE',
            - 'K_S'

        'TERMINATION_ID' und 'TERMINATION_QUANTITY' müssen eingegeben werden!

        :param stage_data: Enthält alle erforderlichen Parameter in der Form {Schlüssel: Wert}
        :type stage_data: dict
        """        '''

        '''

        # allowed key names
        variable_names_pd = [
        'TERMINATION_ID',
        'TERMINATION_QUANTITY',
        'DT_MAX',
        'FLOW_RATE',
        'P_BOUNDARY_CONDITION',
        'BOUNDARY_PRESSURE',
        'T_BOUNDARY_CONDITION',
        'BOUNDARY_TEMPERATURE',
        'K_S']

        # check spelling of keys:
        for key in stage_data.keys():
            assert key in variable_names_pd, 'Spelling error %s' %(key)
        assert 'TERMINATION_ID' in stage_data.keys()
        assert 'TERMINATION_QUANTITY' in stage_data.keys()

        # add stage to stages_param
        self.stages_param[self.n_stages] = copy.deepcopy(stage_data)
        self.n_stages += 1


    def export_processData(self,save_folder,project_name, suffix = ''):
        """Exports class to a txt-File with the suffix '_gaca.pd.txt'.
        Will will be exported to a folder named (path, project_name, suffix). If it does not exist, it will be created.

        :param save_folder: _description_
        :type save_folder: str
        :param project_name: _description_
        :type project_name: str
        :param suffix: defaults to ''
        :type suffix: str, optional
        """     
        save_path = os.path.join(save_folder, project_name, suffix)
        if not (os.path.exists(save_path)):
            os.makedirs(save_path)
            print('Created new folder %s' %(save_path))
        file_name =  os.path.join(save_path, project_name + suffix + '_gaca.pd.txt')
        fid = open(file_name, 'w')

        def write_kwargs2Fid(data,fid):
            if isinstance(data,int): 
                fid.write('\t%d'%(data))
            elif isinstance(data,float):
                fid.write('\t%.2f'%(data))
            elif isinstance(data,list):
                fid.write('\n%s\n'%('\t'.join(str(element) for element in data)))
            elif isinstance(data, str):
                fid.write('\t%s\n'%(data))
            elif type(data).__module__ == np.__name__:
                fid.write('\n')
                data.tofile(fid,sep='\t',format='%.2f')
                fid.write('\n')
            

        fid.write('DESCRIPTION\t%s\n' %(self.description))																	
        fid.write('N_FLUID\t%d\n' %(self.n_fluid)	)														
        fid.write('NUMBER_OF_STAGES [/]\t%d\n\n' %(self.n_stages)	)														
        fid.write('MEDIUM_TYPE\n%s\n\n' %('\t'.join(self.medium_type))	)
        fid.write('MEDIUM_ID\n%s\n\n' %('\t'.join(str(elem) for elem in self.medium_id))	)    
        fid.write('COUPLED_ANNULI\t# [integer required!]')
        write_kwargs2Fid(self.coupled_annuli,fid)    
        fid.write('\n')

        for i_stage in range(self.n_stages):
            fid.write('\n\n# ++++++++++++++++++++++++++++++++\n')
            fid.write('STAGE\t%d\n' %(i_stage + 1)	)
            for key, value in self.stages_param[i_stage].items():
                fid.write('\n%s' %(key))
                write_kwargs2Fid(value,fid)

        fid.close()
        print('Run sucessfull')
        print(file_name)

####################################################################################

