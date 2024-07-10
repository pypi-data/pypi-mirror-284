
from abc import ABC, abstractmethod

from .fcscore import ( 
    ColorSelection, 
    GEOM_Object,
    Mesh,
    Model
)

from .fcsoptions import (
    ContainerTypes,
    DataTypes,
    
)
from .fcsoptions import (
    StatusMessageType,
    ProcessExitStatus
)

from .geometrybuilder import GeometryBuilder

class CloudModelCommunicatorBase(ABC):
    """
    Defines interface class that specified available commands that can be sent 
    to the frontend viewer directly via websocket connections.

    All plugins are restricted to use methods available in this interface to communicate
    changes to cloud models.
    """
    def __init__(self):
        self.geometry_builder: GeometryBuilder = None
        self.model_builder: Model = None

    ################################################################################################
    #                           Cloud Model - Visibility Operations
    ################################################################################################

    @abstractmethod
    def hide(self, instance_id: int) -> None:
        """
        Hides items in the viewer.
        """

    @abstractmethod
    def hide_only(self, instance_id: int) -> None:
        """
        Only sets this given item to be hidden all the rest will be shown.
        """

    @abstractmethod
    def hide_all(self) -> None:
        """
        Hides everything in the active model             
        """

    @abstractmethod
    def show(self, instance_id: int) -> None:
        """
        Pass in unique ID of the object to activate entity in the viewer.              
        """

    @abstractmethod
    def show_only(self, instance_id: int) -> None:
        """
        Pass in unique ID of the object to show that entity only                
        """

    @abstractmethod
    def show_all(self) -> None:
        """
        Displays all entities in the viewer.
        """

    @abstractmethod
    def set_transparency(self, instance_id: int, opacity: float) -> None:
        """
        Sets transparency of the object in the viewer.
        """

    @abstractmethod
    def center_view(self) -> None:
        """
        Adjust camera that all is visible 
        """
        
    ################################################################################################
    #                           Cloud Model - High-Level Operations
    ################################################################################################

    @abstractmethod
    def get_model_output_directory(self) -> str:
        """
        Returns full path to root of the working directory.
        """
        
    @abstractmethod
    def set_model_name(self, model_name: str) -> None:
        """
        Renames the workspace binary. Do not include extension!
        """
        
    @abstractmethod
    def get_model_name(self) -> str:
        """
        Returns the core model file name without extension.
        """

    @abstractmethod
    def clear_model(self) -> bool:
        """Clears the document and discards all entities in it.

        Returns:
            bool: If the document clearing was successful.
        """

    @abstractmethod
    def open_new_model(self, new_model_name: str) -> None:
        """
        Sets a new model name.
        """

    @abstractmethod
    def commit_to_model(self) -> bool:
        """
        If we commit to a document it is deserialised into a file in the local working folder
        and it is uploaded to the server to synchronise with the server's working instance.

        This will enable 'Active' mode in the viewer allowing the user to actively
        interact / modify / export the model generated by the plugin. 
        """
    
    ################################################################################################
    #                           Cloud Model - Data Operations
    ################################################################################################

    @abstractmethod
    def add_container(self, name: str, container_type: DataTypes) -> int:
        """
        Creates a TOP LEVEL empty container that will not store any geometric objects 
        at its unique ID. It is used to group together and organize other entities
        in the model tree.
        """

    @abstractmethod
    def add_folder(self, folder_name: str, parent_id: int, folder_type: DataTypes=DataTypes.Assembly) -> int:
        """
        Creates an empty folder NESTED UNDER A PARENT that will not store any geometric 
        objects at its unique ID. It is used to group together and organize other entities
        in the model tree.
        """
    
    @abstractmethod
    def add_file(self, file_name: str, parent_id: int, file_type: DataTypes=DataTypes.Part) -> int:
        """
        Creates an empty folder NESTED UNDER A PARENT that will not store any geometric 
        objects at its unique ID. It is used to group together and organize other entities
        in the model tree.
        """

    @abstractmethod
    def add_mesh_to_model(self,
                          mesh_entity: Mesh,
                          mesh_instance_name: str, 
                          parent_instance_id: int, 
                          is_visible: bool = False) -> int:
        """
        Adds mesh entity under a parent entity.
        Returns associateed file ID.
        """

    @abstractmethod
    def add_geom_to_model(self, 
                     geom_entity: GEOM_Object, 
                     parent_instance_id: int, 
                     geom_instance_name: str,
                     is_visible: bool = False, 
                     add_with_refined_resolution: bool = True) -> int:
        """
        Adds geometric entity under a parent entity
        Returns associateed file ID.
        """

    @abstractmethod
    def remove_from_model(self, instance_id: int) -> None:
        """
        Removes all child entities under this ID. 
        All components that were removed from the document
        need to be updated. The removed_ids must contain the passed in ID itself.
        """
    
    @abstractmethod
    def set_specific_instance_color(self, id: int, red: int, green: int, blue: int) -> None:
        """
        Colours object in viewer. 
        Input are RGB integers between 0 to 255.
        """

    @abstractmethod
    def set_instance_color(self, id: int, selected_color: ColorSelection) -> None:
        """
        Colours object in viewer.

        Input is a specific colour that is available in the selection.
        """
        
    @abstractmethod
    def find_instance_from_viewer_by_name(self, name: str) -> list:
        """
        Returns all objects that can be found under the specified under
        the specified name.
        """
    
    ################################################################################################
    #                           Cloud Model - Transformation Operations
    ################################################################################################
       
    @abstractmethod
    def translate_by_dxdydz(self, instance_id: int, vector_xyz: list) -> GEOM_Object | None:
       """
       Eltol egy vektor altal megadott iranyba es a vektor meretevel
       """
       
    @abstractmethod
    def translate_by_two_points(self, instance1_id: int, object2_id: int, object3_id: int):
       """
       Eltol ket pont altal meghatarozott iranyba, a pontok kozti tavolsag metekevel

       arg1: objectumok (most csak faces), amiken az eltolast vegezzuk
       arg2: pont1
       arg2: pont2

       Todo: az instance1_id-nak egy listanak kellene lennie, ami id-kat tartalmaz
       """
       
   ################################################################################################
   #                           Cloud Model - State Operations
   ################################################################################################

    @abstractmethod
    def show_message(self, message: str) -> None:
       """Creates a pop-up window to the user.

       Args:
           message (str): The message to be shown in the pop-up window.
       """

    @abstractmethod
    def refresh_viewer(self) -> bool:
        """
        By default, the viewer is not rendering any added/removed/modified components,
        unless we are operating on views (view centering, camera position, etc.)
        """
    
    @abstractmethod
    def update_viewer(self) -> None:
        """
        Updates viewer's document. Will load all added entities to the viewer               
        Legacy functionality: `salome.sg.updateObjBrowser()`
        """
        
    @abstractmethod
    def show_progress_tracker(self, 
                              progress_percentage: float,
                              current_process_name: str, 
                              process_bundle_title: str='') -> None:
        """
        Can be used to communicate to the user the progress of a backend process.

        Args:
            progress_percentage (float): Has to be a value between 0 and 100. If is outside
                of these bounds an exception is thrown!
            current_process_name (str): Need to name the process that's running, or provide 
                some description otherwise it will throw an error
            process_bundle_title (str, optional): This will override the title of the dialog,
                by default its empty and is not overridden.
        """

    @abstractmethod
    def finish_progress_tracker(self, 
                                exit_status: ProcessExitStatus=ProcessExitStatus.Successful, 
                                exit_message: str='Operation Completed!', 
                                immediate_shutdown=False) -> None:
        """
        This will finish the progress tracking.

        Args:
            exit_status (bool, optional): Based on the exit status the dialog will change slightly in style.
            exit_message (str, optional): What should be shown to the user when the process finished. Defaults to 'Operation Completed!'.
            immediate_shutdown (bool, optional): If set to true, the progress tracker will immediately disappear. Defaults to False.
        """

    @abstractmethod
    def show_status_message(self, message_type: StatusMessageType, message: str) -> None:
        """
        Propagates an info, warning, or error message to the frontend client.
        """