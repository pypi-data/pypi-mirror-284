 
from biopax.control import Control
##############################
 


 
from biopax.utils.class_utils import tostring,tojson
from biopax.utils.validate_utils import CValidateArgType,raise_error





validator = CValidateArgType(raise_error, logger=None)

@tostring
class Catalysis(Control) :


    """
    Class Catalysis 
    
        
          Definition: A control interaction in which a physical entity (a catalyst)
      increases the rate of a conversion interaction by lowering its activation
      energy. Instances of this class describe a pairing between a catalyzing entity
      and a catalyzed conversion. Rationale: Catalysis, theoretically, is always
      bidirectional since it acts by lowering the activation energy. Physiologically,
      however, it can have a direction because of the concentration of the
      participants. For example, the oxidative decarboxylation catalyzed by Isocitrate
      dehydrogenase always happens in one direction under physiological conditions
      since the produced carbon dioxide is constantly removed from the system.
      Usage: A separate catalysis instance should be created for each different
      conversion that a physicalEntity may catalyze and for each different
      physicalEntity that may catalyze a conversion. For example, a bifunctional
      enzyme that catalyzes two different biochemical reactions would be linked to
      each of those biochemical reactions by two separate instances of the catalysis
      class. Also, catalysis reactions from multiple different organisms could be
      linked to the same generic biochemical reaction (a biochemical reaction is
      generic if it only includes small molecules). Generally, the enzyme catalyzing a
      conversion is known and the use of this class is obvious, however, in the cases
      where a catalyzed reaction is known to occur but the enzyme is not known, a
      catalysis instance can be created without a controller specified. Synonyms:
      facilitation, acceleration. Examples: The catalysis of a biochemical reaction by
      an enzyme, the enabling of a transport interaction by a membrane pore complex,
      and the facilitation of a complex assembly by a scaffold protein. Hexokinase ->
      (The "Glucose + ATP -> Glucose-6-phosphate +ADP" reaction). A plasma membrane
      Na+/K+ ATPase is an active transporter (antiport pump) using the energy of ATP
      to pump Na+ out of the cell and K+ in. Na+ from cytoplasm to extracellular space
      would be described in a transport instance. K+ from extracellular space to
      cytoplasm would be described in a transport instance. The ATPase pump would be
      stored in a catalysis instance controlling each of the above transport
      instances. A biochemical reaction that does not occur by itself under
      physiological conditions, but has been observed to occur in the presence of cell
      extract, likely via one or more unknown enzymes present in the extract, would be
      stored in the CONTROLLED property, with the CONTROLLER property empty.

    
    code generator : rdfobj (author F.Moreews 2023-2024).
    
    """

    ##########constructor

    def __init__(self, *args, **kwargs):
        #args -- tuple of anonymous arguments
        #kwargs -- dictionary of named arguments
        
        self.pk=kwargs.get('pk',None)    
        self.pop_state=kwargs.get('pop_state',None)  
        self.exhausted=kwargs.get('exhausted',None)
        self.meta_label=None  
        
        super().__init__(*args, **kwargs) 
        self.rdf_type="http://www.biopax.org/release/biopax-level3.owl#Catalysis"
        self._cofactor=kwargs.get('cofactor',None)  
        self._catalysisDirection=kwargs.get('catalysisDirection',None)  
        self._controlled=kwargs.get('controlled',None)  
        self._controller=kwargs.get('controller',None)  
        self._controlType=kwargs.get('controlType',None)  
        self._controlled=kwargs.get('controlled',None)  
        self._controller=kwargs.get('controller',None)  
        self._controlType=kwargs.get('controlType',None)  
        self._controlled=kwargs.get('controlled',None)  
        self._controller=kwargs.get('controller',None)  
        self._controlType=kwargs.get('controlType',None)  
  

##########getter
     
    def get_cofactor(self):
        """
        Attribute _cofactor  getter
                      Any cofactor(s) or coenzyme(s) required for catalysis of the conversion by the
      enzyme. This is a suproperty of participants.

                """
        return self._cofactor  
     
    def get_catalysisDirection(self):
        """
        Attribute _catalysisDirection  getter
                      This property represents the direction of this catalysis under all physiological
      conditions if there is one.  Note that chemically a catalyst will increase the
      rate of the reaction in both directions. In biology, however, there are cases
      where the enzyme is expressed only when the controlled bidirectional conversion
      is on one side of the chemical equilibrium. For example E.Coli's lac operon
      ensures that lacZ gene is only synthesized when there is enough lactose in the
      medium.  If that is the case and the controller, under biological conditions, is
      always catalyzing the conversion in one direction then this fact can be captured
      using this property. If the enzyme is active for both directions, or the
      conversion is not bidirectional, this property should be left empty.

                """
        return self._catalysisDirection  
     
    def get_controlled(self):
        """
        Attribute _controlled  getter
                      The entity that is controlled, e.g., in a biochemical reaction, the reaction is
      controlled by an enzyme. Controlled is a sub-property of participants.

                """
        return self._controlled  
     
    def get_controller(self):
        """
        Attribute _controller  getter
                      The controlling entity, e.g., in a biochemical reaction, an enzyme is the
      controlling entity of the reaction. CONTROLLER is a sub-property of
      PARTICIPANTS.

                """
        return self._controller  
     
    def get_controlType(self):
        """
        Attribute _controlType  getter
                      Defines the nature of the control relationship between the controller and the
      controlled entities.  The following terms are possible values:  ACTIVATION:
      General activation. Compounds that activate the specified enzyme activity by an
      unknown mechanism. The mechanism is defined as unknown, because either the
      mechanism has yet to be elucidated in the experimental literature, or the
      paper(s) curated thus far do not define the mechanism, and a full literature
      search has yet to be performed.  The following term can not be used in the
      catalysis class: INHIBITION: General inhibition. Compounds that inhibit the
      specified enzyme activity by an unknown mechanism. The mechanism is defined as
      unknown, because either the mechanism has yet to be elucidated in the
      experimental literature, or the paper(s) curated thus far do not define the
      mechanism, and a full literature search has yet to be performed.  The following
      terms can only be used in the modulation class (these definitions from EcoCyc):
      INHIBITION-ALLOSTERIC Allosteric inhibitors decrease the specified enzyme
      activity by binding reversibly to the enzyme and inducing a conformational
      change that decreases the affinity of the enzyme to its substrates without
      affecting its VMAX. Allosteric inhibitors can be competitive or noncompetitive
      inhibitors, therefore, those inhibition categories can be used in conjunction
      with this category.  INHIBITION-COMPETITIVE Competitive inhibitors are compounds
      that competitively inhibit the specified enzyme activity by binding reversibly
      to the enzyme and preventing the substrate from binding. Binding of the
      inhibitor and substrate are mutually exclusive because it is assumed that the
      inhibitor and substrate can both bind only to the free enzyme. A competitive
      inhibitor can either bind to the active site of the enzyme, directly excluding
      the substrate from binding there, or it can bind to another site on the enzyme,
      altering the conformation of the enzyme such that the substrate can not bind to
      the active site.  INHIBITION-IRREVERSIBLE Irreversible inhibitors are compounds
      that irreversibly inhibit the specified enzyme activity by binding to the enzyme
      and dissociating so slowly that it is considered irreversible. For example,
      alkylating agents, such as iodoacetamide, irreversibly inhibit the catalytic
      activity of some enzymes by modifying cysteine side chains.  INHIBITION-
      NONCOMPETITIVE Noncompetitive inhibitors are compounds that noncompetitively
      inhibit the specified enzyme by binding reversibly to both the free enzyme and
      to the enzyme-substrate complex. The inhibitor and substrate may be bound to the
      enzyme simultaneously and do not exclude each other. However, only the enzyme-
      substrate complex (not the enzyme-substrate-inhibitor complex) is catalytically
      active.  INHIBITION-OTHER Compounds that inhibit the specified enzyme activity
      by a mechanism that has been characterized, but that cannot be clearly
      classified as irreversible, competitive, noncompetitive, uncompetitive, or
      allosteric.  INHIBITION-UNCOMPETITIVE Uncompetitive inhibitors are compounds
      that uncompetitively inhibit the specified enzyme activity by binding reversibly
      to the enzyme-substrate complex but not to the enzyme alone.  ACTIVATION-
      NONALLOSTERIC Nonallosteric activators increase the specified enzyme activity by
      means other than allosteric.  ACTIVATION-ALLOSTERIC Allosteric activators
      increase the specified enzyme activity by binding reversibly to the enzyme and
      inducing a conformational change that increases the affinity of the enzyme to
      its substrates without affecting its VMAX.

                """
        return self._controlType  
     
    def get_controlled(self):
        """
        Attribute _controlled  getter
                      The entity that is controlled, e.g., in a biochemical reaction, the reaction is
      controlled by an enzyme. Controlled is a sub-property of participants.

                """
        return self._controlled  
     
    def get_controller(self):
        """
        Attribute _controller  getter
                      The controlling entity, e.g., in a biochemical reaction, an enzyme is the
      controlling entity of the reaction. CONTROLLER is a sub-property of
      PARTICIPANTS.

                """
        return self._controller  
     
    def get_controlType(self):
        """
        Attribute _controlType  getter
                      Defines the nature of the control relationship between the controller and the
      controlled entities.  The following terms are possible values:  ACTIVATION:
      General activation. Compounds that activate the specified enzyme activity by an
      unknown mechanism. The mechanism is defined as unknown, because either the
      mechanism has yet to be elucidated in the experimental literature, or the
      paper(s) curated thus far do not define the mechanism, and a full literature
      search has yet to be performed.  The following term can not be used in the
      catalysis class: INHIBITION: General inhibition. Compounds that inhibit the
      specified enzyme activity by an unknown mechanism. The mechanism is defined as
      unknown, because either the mechanism has yet to be elucidated in the
      experimental literature, or the paper(s) curated thus far do not define the
      mechanism, and a full literature search has yet to be performed.  The following
      terms can only be used in the modulation class (these definitions from EcoCyc):
      INHIBITION-ALLOSTERIC Allosteric inhibitors decrease the specified enzyme
      activity by binding reversibly to the enzyme and inducing a conformational
      change that decreases the affinity of the enzyme to its substrates without
      affecting its VMAX. Allosteric inhibitors can be competitive or noncompetitive
      inhibitors, therefore, those inhibition categories can be used in conjunction
      with this category.  INHIBITION-COMPETITIVE Competitive inhibitors are compounds
      that competitively inhibit the specified enzyme activity by binding reversibly
      to the enzyme and preventing the substrate from binding. Binding of the
      inhibitor and substrate are mutually exclusive because it is assumed that the
      inhibitor and substrate can both bind only to the free enzyme. A competitive
      inhibitor can either bind to the active site of the enzyme, directly excluding
      the substrate from binding there, or it can bind to another site on the enzyme,
      altering the conformation of the enzyme such that the substrate can not bind to
      the active site.  INHIBITION-IRREVERSIBLE Irreversible inhibitors are compounds
      that irreversibly inhibit the specified enzyme activity by binding to the enzyme
      and dissociating so slowly that it is considered irreversible. For example,
      alkylating agents, such as iodoacetamide, irreversibly inhibit the catalytic
      activity of some enzymes by modifying cysteine side chains.  INHIBITION-
      NONCOMPETITIVE Noncompetitive inhibitors are compounds that noncompetitively
      inhibit the specified enzyme by binding reversibly to both the free enzyme and
      to the enzyme-substrate complex. The inhibitor and substrate may be bound to the
      enzyme simultaneously and do not exclude each other. However, only the enzyme-
      substrate complex (not the enzyme-substrate-inhibitor complex) is catalytically
      active.  INHIBITION-OTHER Compounds that inhibit the specified enzyme activity
      by a mechanism that has been characterized, but that cannot be clearly
      classified as irreversible, competitive, noncompetitive, uncompetitive, or
      allosteric.  INHIBITION-UNCOMPETITIVE Uncompetitive inhibitors are compounds
      that uncompetitively inhibit the specified enzyme activity by binding reversibly
      to the enzyme-substrate complex but not to the enzyme alone.  ACTIVATION-
      NONALLOSTERIC Nonallosteric activators increase the specified enzyme activity by
      means other than allosteric.  ACTIVATION-ALLOSTERIC Allosteric activators
      increase the specified enzyme activity by binding reversibly to the enzyme and
      inducing a conformational change that increases the affinity of the enzyme to
      its substrates without affecting its VMAX.

                """
        return self._controlType  
     
    def get_controlled(self):
        """
        Attribute _controlled  getter
                      The entity that is controlled, e.g., in a biochemical reaction, the reaction is
      controlled by an enzyme. Controlled is a sub-property of participants.

                """
        return self._controlled  
     
    def get_controller(self):
        """
        Attribute _controller  getter
                      The controlling entity, e.g., in a biochemical reaction, an enzyme is the
      controlling entity of the reaction. CONTROLLER is a sub-property of
      PARTICIPANTS.

                """
        return self._controller  
     
    def get_controlType(self):
        """
        Attribute _controlType  getter
                      Defines the nature of the control relationship between the controller and the
      controlled entities.  The following terms are possible values:  ACTIVATION:
      General activation. Compounds that activate the specified enzyme activity by an
      unknown mechanism. The mechanism is defined as unknown, because either the
      mechanism has yet to be elucidated in the experimental literature, or the
      paper(s) curated thus far do not define the mechanism, and a full literature
      search has yet to be performed.  The following term can not be used in the
      catalysis class: INHIBITION: General inhibition. Compounds that inhibit the
      specified enzyme activity by an unknown mechanism. The mechanism is defined as
      unknown, because either the mechanism has yet to be elucidated in the
      experimental literature, or the paper(s) curated thus far do not define the
      mechanism, and a full literature search has yet to be performed.  The following
      terms can only be used in the modulation class (these definitions from EcoCyc):
      INHIBITION-ALLOSTERIC Allosteric inhibitors decrease the specified enzyme
      activity by binding reversibly to the enzyme and inducing a conformational
      change that decreases the affinity of the enzyme to its substrates without
      affecting its VMAX. Allosteric inhibitors can be competitive or noncompetitive
      inhibitors, therefore, those inhibition categories can be used in conjunction
      with this category.  INHIBITION-COMPETITIVE Competitive inhibitors are compounds
      that competitively inhibit the specified enzyme activity by binding reversibly
      to the enzyme and preventing the substrate from binding. Binding of the
      inhibitor and substrate are mutually exclusive because it is assumed that the
      inhibitor and substrate can both bind only to the free enzyme. A competitive
      inhibitor can either bind to the active site of the enzyme, directly excluding
      the substrate from binding there, or it can bind to another site on the enzyme,
      altering the conformation of the enzyme such that the substrate can not bind to
      the active site.  INHIBITION-IRREVERSIBLE Irreversible inhibitors are compounds
      that irreversibly inhibit the specified enzyme activity by binding to the enzyme
      and dissociating so slowly that it is considered irreversible. For example,
      alkylating agents, such as iodoacetamide, irreversibly inhibit the catalytic
      activity of some enzymes by modifying cysteine side chains.  INHIBITION-
      NONCOMPETITIVE Noncompetitive inhibitors are compounds that noncompetitively
      inhibit the specified enzyme by binding reversibly to both the free enzyme and
      to the enzyme-substrate complex. The inhibitor and substrate may be bound to the
      enzyme simultaneously and do not exclude each other. However, only the enzyme-
      substrate complex (not the enzyme-substrate-inhibitor complex) is catalytically
      active.  INHIBITION-OTHER Compounds that inhibit the specified enzyme activity
      by a mechanism that has been characterized, but that cannot be clearly
      classified as irreversible, competitive, noncompetitive, uncompetitive, or
      allosteric.  INHIBITION-UNCOMPETITIVE Uncompetitive inhibitors are compounds
      that uncompetitively inhibit the specified enzyme activity by binding reversibly
      to the enzyme-substrate complex but not to the enzyme alone.  ACTIVATION-
      NONALLOSTERIC Nonallosteric activators increase the specified enzyme activity by
      means other than allosteric.  ACTIVATION-ALLOSTERIC Allosteric activators
      increase the specified enzyme activity by binding reversibly to the enzyme and
      inducing a conformational change that increases the affinity of the enzyme to
      its substrates without affecting its VMAX.

                """
        return self._controlType  
  
##########setter
    
    @validator(value="biopax.PhysicalEntity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_cofactor(self,value):
        self._cofactor=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_catalysisDirection(self,value):
        enum_val=['LEFT-TO-RIGHT', 'RIGHT-TO-LEFT']
        if value not in enum_val:
           raise Exception("value of catalysisDirection not in   ['LEFT-TO-RIGHT', 'RIGHT-TO-LEFT']")
        self._catalysisDirection=value  
    
    @validator(value="biopax.Entity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_controlled(self,value):
        self._controlled=value  
    
    @validator(value="biopax.Entity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_controller(self,value):
        self._controller=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_controlType(self,value):
        enum_val=['INHIBITION', 'ACTIVATION', 'INHIBITION-ALLOSTERIC', 'INHIBITION-COMPETITIVE', 'INHIBITION-IRREVERSIBLE', 'INHIBITION-NONCOMPETITIVE', 'INHIBITION-OTHER', 'INHIBITION-UNCOMPETITIVE', 'ACTIVATION-NONALLOSTERIC', 'ACTIVATION-ALLOSTERIC']
        if value not in enum_val:
           raise Exception("value of controlType not in   ['INHIBITION', 'ACTIVATION', 'INHIBITION-ALLOSTERIC', 'INHIBITION-COMPETITIVE', 'INHIBITION-IRREVERSIBLE', 'INHIBITION-NONCOMPETITIVE', 'INHIBITION-OTHER', 'INHIBITION-UNCOMPETITIVE', 'ACTIVATION-NONALLOSTERIC', 'ACTIVATION-ALLOSTERIC']")
        self._controlType=value  
    
    @validator(value="biopax.Entity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_controlled(self,value):
        self._controlled=value  
    
    @validator(value="biopax.Entity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_controller(self,value):
        self._controller=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_controlType(self,value):
        enum_val=['INHIBITION', 'ACTIVATION', 'INHIBITION-ALLOSTERIC', 'INHIBITION-COMPETITIVE', 'INHIBITION-IRREVERSIBLE', 'INHIBITION-NONCOMPETITIVE', 'INHIBITION-OTHER', 'INHIBITION-UNCOMPETITIVE', 'ACTIVATION-NONALLOSTERIC', 'ACTIVATION-ALLOSTERIC']
        if value not in enum_val:
           raise Exception("value of controlType not in   ['INHIBITION', 'ACTIVATION', 'INHIBITION-ALLOSTERIC', 'INHIBITION-COMPETITIVE', 'INHIBITION-IRREVERSIBLE', 'INHIBITION-NONCOMPETITIVE', 'INHIBITION-OTHER', 'INHIBITION-UNCOMPETITIVE', 'ACTIVATION-NONALLOSTERIC', 'ACTIVATION-ALLOSTERIC']")
        self._controlType=value  
    
    @validator(value="biopax.Entity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_controlled(self,value):
        self._controlled=value  
    
    @validator(value="biopax.Entity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_controller(self,value):
        self._controller=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_controlType(self,value):
        enum_val=['INHIBITION', 'ACTIVATION', 'INHIBITION-ALLOSTERIC', 'INHIBITION-COMPETITIVE', 'INHIBITION-IRREVERSIBLE', 'INHIBITION-NONCOMPETITIVE', 'INHIBITION-OTHER', 'INHIBITION-UNCOMPETITIVE', 'ACTIVATION-NONALLOSTERIC', 'ACTIVATION-ALLOSTERIC']
        if value not in enum_val:
           raise Exception("value of controlType not in   ['INHIBITION', 'ACTIVATION', 'INHIBITION-ALLOSTERIC', 'INHIBITION-COMPETITIVE', 'INHIBITION-IRREVERSIBLE', 'INHIBITION-NONCOMPETITIVE', 'INHIBITION-OTHER', 'INHIBITION-UNCOMPETITIVE', 'ACTIVATION-NONALLOSTERIC', 'ACTIVATION-ALLOSTERIC']")
        self._controlType=value  
  




    def object_attributes(self):

      object_attribute_list=super().object_attributes() 
      satt=['cofactor']
      for elem in satt:
        object_attribute_list.append(elem)
      return object_attribute_list
 

    def type_attributes(self):
 
      type_attribute_list=super().type_attributes() 
      satt=['catalysisDirection']
      for elem in satt:
        type_attribute_list.append(elem)
      return type_attribute_list
 
#####get attributes types 
    def attribute_type_by_name(self):
      ma=dict()
      ma=super().attribute_type_by_name() 
      ma['cofactor']='PhysicalEntity'  
      ma['catalysisDirection']='str'  
      ma['controlled']='Entity'  
      ma['controller']='Entity'  
      ma['controlType']='str'  
      ma['controlled']='Entity'  
      ma['controller']='Entity'  
      ma['controlType']='str'  
      ma['controlled']='Entity'  
      ma['controller']='Entity'  
      ma['controlType']='str'  
      return ma



    def to_json(self):
        return tojson(self)
        

    def get_uri_string(self):
        return self.pk

    def set_uri_string(self,uristr):
        self.pk= uristr       