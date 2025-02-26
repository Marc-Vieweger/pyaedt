"""This module contains these classes: ``RMXprtModule`` and ``Rmxprt``."""
from __future__ import absolute_import  # noreorder

from pyaedt.application.AnalysisRMxprt import FieldAnalysisRMxprt
from pyaedt.generic.general_methods import pyaedt_function_handler


class RMXprtModule(object):
    """Provides RMxprt module properties."""

    component = None
    prop_servers = None

    @pyaedt_function_handler()
    def get_prop_server(self, parameter_name):
        """Retrieve the properties of the server.

        Parameters
        ----------
        parameter_name : str
            Name of the server.


        Returns
        -------
        list
            List of server properties.

        """
        prop_server = None
        for key, parameter_list in self.prop_servers.items():
            if parameter_name in parameter_list:
                prop_server = key
                break
        assert prop_server is not None, "Unknown parameter name {0} exists in component {1}.".format(
            prop_server, self.component
        )
        return prop_server

    def __init__(self, oeditor):
        self.oeditor = oeditor

    @pyaedt_function_handler()
    def __setitem__(self, parameter_name, value):
        self.set_rmxprt_parameter(parameter_name, value)
        return True

    @pyaedt_function_handler()
    def __getitem__(self, parameter_name):
        prop_server = self.get_prop_server(parameter_name)
        separator = ":" if prop_server else ""
        val = self.oeditor.GetPropertyValue(
            self.component, "{0}{1}{2}".format(self.component, separator, prop_server), parameter_name
        )
        return val

    @pyaedt_function_handler()
    def set_rmxprt_parameter(self, parameter_name, value):
        """Modify a parameter value.

        Parameters
        ----------
        parameter_name : str
            Name of the parameter.
        value :
            Value to assign to the parameter.

        Returns
        -------
        bool
            ``True`` when successful, ``False`` when failed

        References
        ----------

        >>> oEditor.ChangeProperty
        """
        prop_server = self.get_prop_server(parameter_name)
        separator = ":" if prop_server else ""
        self.oeditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:" + self.component,
                    ["NAME:PropServers", "{0}{1}{2}".format(self.component, separator, prop_server)],
                    ["NAME:ChangedProps", ["NAME:" + parameter_name, "Value:=", value]],
                ],
            ]
        )
        return True


class Stator(RMXprtModule):
    """Provides stator properties."""

    component = "Stator"
    prop_servers = {
        "": [
            "Outer Diameter",
            "Inner Diameter",
            "Length",
            "Stacking Factor" "Steel Type",
            "Number of Slots",
            "Slot Type",
            "Lamination Sectors",
            "Press Board Thickness",
            "Skew Width",
        ],
        "Slot": ["Hs0", "Hs1", "Hs2", "Bs0", "Bs1", "Bs2"],
        "Winding": ["Winding Type", "Parallel Branches"],
    }


class Rotor(RMXprtModule):
    """Provides rotor properties."""

    component = "Rotor"
    prop_servers = {"": ["Outer Diameter"], "Slot": [], "Winding": []}


class Rmxprt(FieldAnalysisRMxprt):
    """Provides the RMxprt application interface.

    Parameters
    ----------
    projectname : str, optional
        Name of the project to select or the full path to the project
        or AEDTZ archive to open. The default is ``None``, in which
        case an attempt is made to get an active project. If no
        projects are present, an empty project is created.
    designname : str, optional
        Name of the design to select. The default is ``None``, in
        which case an attempt is made to get an active design. If no
        designs are present, an empty design is created.
    solution_type : str, optional
        Solution type to apply to the design. The default is
        ``None``, in which ase the default type is applied.
    model_units : str, optional
        Model units.
    setup_name : str, optional
        Name of the setup to use as the nominal. The default is
        ``None``, in which case the active setup is used or
        nothing is used.
    specified_version : str, optional
        Version of AEDT to use. The default is ``None``, in which case
        the active setup is used or the latest installed version is
        used.
    non_graphical : bool, optional
        Whether to launch AEDT in non-graphical mode. The default
        is ``False``, in which case AEDT is launched in graphical mode.
        This parameter is ignored when a script is launched within AEDT.
    new_desktop_session : bool, optional
        Whether to launch an instance of AEDT in a new thread, even if
        another instance of the ``specified_version`` is active on the
        machine.  The default is ``True``.
    close_on_exit : bool, optional
        Whether to release AEDT on exit. The default is ``True``.
    student_version : bool, optional
        Whether to open the AEDT student version. The default is ``False``.
    machine : str, optional
        Machine name to which connect the oDesktop Session. Works only on 2022R2.
        Remote Server must be up and running with command `"ansysedt.exe -grpcsrv portnum"`.
        If machine is `"localhost"` the server will also start if not present.
    port : int, optional
        Port number of which start the oDesktop communication on already existing server.
        This parameter is ignored in new server creation. It works only on 2022R2.
        Remote Server must be up and running with command `"ansysedt.exe -grpcsrv portnum"`.
    aedt_process_id : int, optional
        Only used when ``new_desktop_session = False``, specifies by process ID which instance
        of Electronics Desktop to point PyAEDT at.

    Examples
    --------
    Create an instance of RMxprt and connect to an existing RMxprt
    design or create a new RMxprt design if one does not exist.

    >>> from pyaedt import Rmxprt
    >>> app = Rmxprt()

    Create an instance of Rmxprt and link to a project named
    ``"projectname"``. If this project does not exist, create one with
    this name.

    >>> app = Rmxprt(projectname)

    Create an instance of RMxprt and link to a design named
    ``"designname"`` in a project named ``"projectname"``.

    >>> app = Rmxprt(projectname,designame)

    Create an instance of RMxprt and open the specified project,
    which is ``"myfile.aedt"``.

    >>> app = Rmxprt("myfile.aedt")
    """

    def __init__(
        self,
        projectname=None,
        designname=None,
        solution_type=None,
        model_units=None,
        setup_name=None,
        specified_version=None,
        non_graphical=False,
        new_desktop_session=False,
        close_on_exit=False,
        student_version=False,
        machine="",
        port=0,
        aedt_process_id=None,
    ):
        FieldAnalysisRMxprt.__init__(
            self,
            "RMxprtSolution",
            projectname,
            designname,
            solution_type,
            setup_name,
            specified_version,
            non_graphical,
            new_desktop_session,
            close_on_exit,
            student_version,
            machine,
            port,
            aedt_process_id,
        )
        if not model_units or model_units == "mm":
            model_units = "mm"
        else:
            assert model_units == "in", "Invalid model units string {}".format(model_units)
        self.modeler.oeditor.SetMachineUnits(["NAME:Units Parameter", "Units:=", model_units, "Rescale:=", False])
        self.stator = Stator(self.modeler.oeditor)
        self.rotor = Rotor(self.modeler.oeditor)

    def __enter__(self):
        return self

    @property
    def design_type(self):
        """Machine design type."""
        return self.design_solutions.design_type

    @design_type.setter
    @pyaedt_function_handler()
    def design_type(self, value):
        self.design_solutions.design_type = value
