 
from biopax.conversion import Conversion
##############################
 


 
from biopax.utils.class_utils import tostring,tojson
from biopax.utils.validate_utils import CValidateArgType,raise_error





validator = CValidateArgType(raise_error, logger=None)

@tostring
class Degradation(Conversion) :


    """
    Class Degradation 
    
        
          Definition: A conversion in which a pool of macromolecules are degraded into
      their elementary units.  Usage: This conversion always has a direction of left-
      to-right and is irreversible. Degraded molecules are always represented on the
      left, degradation products on the right.   Comments: Degradation is a complex
      abstraction over multiple reactions. Although it obeys law of mass conservation
      and stoichiometric, the products are rarely specified since they are ubiquitous.
      Example:  Degradation of a protein to amino acids.

    
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
        self.rdf_type="http://www.biopax.org/release/biopax-level3.owl#Degradation"
        self._left=kwargs.get('left',None)  
        self._participantStoichiometry=kwargs.get('participantStoichiometry',None)  
        self._right=kwargs.get('right',None)  
        self._conversionDirection=kwargs.get('conversionDirection',None)  
        self._spontaneous=kwargs.get('spontaneous',None)  
        self._cofactor=kwargs.get('cofactor',None)  
        self._controlled=kwargs.get('controlled',None)  
        self._controller=kwargs.get('controller',None)  
        self._interactionType=kwargs.get('interactionType',None)  
        self._left=kwargs.get('left',None)  
        self._participant=kwargs.get('participant',None)  
        self._product=kwargs.get('product',None)  
        self._right=kwargs.get('right',None)  
        self._template=kwargs.get('template',None)  
  

##########getter
     
    def get_left(self):
        """
        Attribute _left  getter
                      The participants on the left side of the conversion interaction. Since
      conversion interactions may proceed in either the left-to-right or right-to-left
      direction, occupants of the left property may be either reactants or products.
      left is a sub-property of participants.

                """
        return self._left  
     
    def get_participantStoichiometry(self):
        """
        Attribute _participantStoichiometry  getter
                      Stoichiometry of the left and right participants.

                """
        return self._participantStoichiometry  
     
    def get_right(self):
        """
        Attribute _right  getter
                      The participants on the right side of the conversion interaction. Since
      conversion interactions may proceed in either the left-to-right or right-to-left
      direction, occupants of the RIGHT property may be either reactants or products.
      RIGHT is a sub-property of PARTICIPANTS.

                """
        return self._right  
     
    def get_conversionDirection(self):
        """
        Attribute _conversionDirection  getter
                      This property represents the direction of the reaction. If a reaction will run
      in a single direction under all biological contexts then it is considered
      irreversible and has a direction. Otherwise it is reversible.

                """
        return self._conversionDirection  
     
    def get_spontaneous(self):
        """
        Attribute _spontaneous  getter
                      Specifies whether a conversion occurs spontaneously or not. If the spontaneity
      is not known, the SPONTANEOUS property should be left empty.

                """
        return self._spontaneous  
     
    def get_cofactor(self):
        """
        Attribute _cofactor  getter
                      Any cofactor(s) or coenzyme(s) required for catalysis of the conversion by the
      enzyme. This is a suproperty of participants.

                """
        return self._cofactor  
     
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
     
    def get_interactionType(self):
        """
        Attribute _interactionType  getter
                      Controlled vocabulary annotating the interaction type for example,
      "phosphorylation reaction". This annotation is meant to be human readable and
      may not be suitable for computing tasks, like reasoning, that require formal
      vocabulary systems. For instance, this information would be useful for display
      on a web page or for querying a database. The PSI-MI interaction type controlled
      vocabulary should be used. This is browsable at:  http://www.ebi.ac.uk/ontology-
      lookup/browse.do?ontName=MI&termId=MI%3A0190&termName=interaction%20type

                """
        return self._interactionType  
     
    def get_left(self):
        """
        Attribute _left  getter
                      The participants on the left side of the conversion interaction. Since
      conversion interactions may proceed in either the left-to-right or right-to-left
      direction, occupants of the left property may be either reactants or products.
      left is a sub-property of participants.

                """
        return self._left  
     
    def get_participant(self):
        """
        Attribute _participant  getter
                      This property lists the entities that participate in this interaction. For
      example, in a biochemical reaction, the participants are the union of the
      reactants and the products of the reaction. This property has a number of sub-
      properties, such as LEFT and RIGHT used in the biochemicalInteraction class. Any
      participant listed in a sub-property will automatically be assumed to also be in
      PARTICIPANTS by a number of software systems, including Protege, so this
      property should not contain any instances if there are instances contained in a
      sub-property.

                """
        return self._participant  
     
    def get_product(self):
        """
        Attribute _product  getter
                      The product of a template reaction.

                """
        return self._product  
     
    def get_right(self):
        """
        Attribute _right  getter
                      The participants on the right side of the conversion interaction. Since
      conversion interactions may proceed in either the left-to-right or right-to-left
      direction, occupants of the RIGHT property may be either reactants or products.
      RIGHT is a sub-property of PARTICIPANTS.

                """
        return self._right  
     
    def get_template(self):
        """
        Attribute _template  getter
                      The template molecule that is used in this template reaction.

                """
        return self._template  
  
##########setter
    
    @validator(value="biopax.PhysicalEntity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_left(self,value):
        self._left=value  
    
    @validator(value="biopax.Stoichiometry", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_participantStoichiometry(self,value):
        self._participantStoichiometry=value  
    
    @validator(value="biopax.PhysicalEntity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_right(self,value):
        self._right=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_conversionDirection(self,value):
        self._conversionDirection=value  
    
    @validator(value="bool", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_spontaneous(self,value):
        self._spontaneous=value  
    
    @validator(value="biopax.PhysicalEntity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_cofactor(self,value):
        self._cofactor=value  
    
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
    
    @validator(value="biopax.InteractionVocabulary", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  1
           #att.nullable:  True
    def set_interactionType(self,value):
        self._interactionType=value  
    
    @validator(value="biopax.PhysicalEntity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_left(self,value):
        self._left=value  
    
    @validator(value="biopax.Entity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_participant(self,value):
        self._participant=value  
    
    @validator(value="biopax.Entity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_product(self,value):
        self._product=value  
    
    @validator(value="biopax.PhysicalEntity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_right(self,value):
        self._right=value  
    
    @validator(value="biopax.Entity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_template(self,value):
        self._template=value  
  




    def object_attributes(self):

      object_attribute_list=super().object_attributes() 
      return object_attribute_list
 

    def type_attributes(self):
 
      type_attribute_list=super().type_attributes() 
      return type_attribute_list
 
#####get attributes types 
    def attribute_type_by_name(self):
      ma=dict()
      ma=super().attribute_type_by_name() 
      ma['left']='PhysicalEntity'  
      ma['participantStoichiometry']='Stoichiometry'  
      ma['right']='PhysicalEntity'  
      ma['conversionDirection']='str'  
      ma['spontaneous']='bool'  
      ma['cofactor']='PhysicalEntity'  
      ma['controlled']='Entity'  
      ma['controller']='Entity'  
      ma['interactionType']='InteractionVocabulary'  
      ma['left']='PhysicalEntity'  
      ma['participant']='Entity'  
      ma['product']='Entity'  
      ma['right']='PhysicalEntity'  
      ma['template']='Entity'  
      return ma



    def to_json(self):
        return tojson(self)
        

    def get_uri_string(self):
        return self.pk

    def set_uri_string(self,uristr):
        self.pk= uristr       