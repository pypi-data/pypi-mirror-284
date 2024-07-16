 
from biopax.utilityclass import UtilityClass
##############################
 


 
from biopax.utils.class_utils import tostring,tojson
from biopax.utils.validate_utils import CValidateArgType,raise_error





validator = CValidateArgType(raise_error, logger=None)

@tostring
class Stoichiometry(UtilityClass) :


    """
    Class Stoichiometry 
    
        
          Definition: Stoichiometric coefficient of a physical entity in the context of a
      conversion or complex. Usage: For each participating element there must be 0 or
      1 stoichiometry element. A non-existing stoichiometric element is treated as
      unknown. This is an n-ary bridge for left, right and component properties.
      Relative stoichiometries ( e.g n, n+1) often used for describing polymerization
      is not supported.

    
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
        self.rdf_type="http://www.biopax.org/release/biopax-level3.owl#Stoichiometry"
        self._physicalEntity=kwargs.get('physicalEntity',None)  
        self._stoichiometricCoefficient=kwargs.get('stoichiometricCoefficient',None)  
        self._comment=kwargs.get('comment',None)  
        self._comment=kwargs.get('comment',None)  
  

##########getter
     
    def get_physicalEntity(self):
        """
        Attribute _physicalEntity  getter
                      The physical entity to be annotated with stoichiometry.

                """
        return self._physicalEntity  
     
    def get_stoichiometricCoefficient(self):
        """
        Attribute _stoichiometricCoefficient  getter
                      Stoichiometric coefficient for one of the entities in an interaction or complex.
      This value can be any rational number. Generic values such as "n" or "n+1"
      should not be used - polymers are currently not covered.

                """
        return self._stoichiometricCoefficient  
     
    def get_comment(self):
        """
        Attribute _comment  getter
                      Comment on the data in the container class. This property should be used instead
      of the OWL documentation elements (rdfs:comment) for instances because
      information in 'comment' is data to be exchanged, whereas the rdfs:comment field
      is used for metadata about the structure of the BioPAX ontology.

                """
        return self._comment  
     
    def get_comment(self):
        """
        Attribute _comment  getter
                      Comment on the data in the container class. This property should be used instead
      of the OWL documentation elements (rdfs:comment) for instances because
      information in 'comment' is data to be exchanged, whereas the rdfs:comment field
      is used for metadata about the structure of the BioPAX ontology.

                """
        return self._comment  
  
##########setter
    
    @validator(value="biopax.PhysicalEntity", nullable=False)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  False
    def set_physicalEntity(self,value):
        self._physicalEntity=value  
    
    @validator(value="float", nullable=False)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  False
    def set_stoichiometricCoefficient(self,value):
        self._stoichiometricCoefficient=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_comment(self,value):
        self._comment=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_comment(self,value):
        self._comment=value  
  




    def object_attributes(self):

      object_attribute_list=super().object_attributes() 
      satt=['physicalEntity']
      for elem in satt:
        object_attribute_list.append(elem)
      return object_attribute_list
 

    def type_attributes(self):
 
      type_attribute_list=super().type_attributes() 
      satt=['stoichiometricCoefficient']
      for elem in satt:
        type_attribute_list.append(elem)
      return type_attribute_list
 
#####get attributes types 
    def attribute_type_by_name(self):
      ma=dict()
      ma=super().attribute_type_by_name() 
      ma['physicalEntity']='PhysicalEntity'  
      ma['stoichiometricCoefficient']='float'  
      ma['comment']='str'  
      ma['comment']='str'  
      return ma



    def to_json(self):
        return tojson(self)
        

    def get_uri_string(self):
        return self.pk

    def set_uri_string(self,uristr):
        self.pk= uristr       