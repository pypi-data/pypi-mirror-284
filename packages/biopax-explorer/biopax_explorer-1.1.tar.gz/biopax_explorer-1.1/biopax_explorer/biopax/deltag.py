 
from biopax.utilityclass import UtilityClass
##############################
 


 
from biopax.utils.class_utils import tostring,tojson
from biopax.utils.validate_utils import CValidateArgType,raise_error





validator = CValidateArgType(raise_error, logger=None)

@tostring
class DeltaG(UtilityClass) :


    """
    Class DeltaG 
    
        
          Definition: Standard transformed Gibbs energy change for a reaction written in
      terms of biochemical reactants.   Usage: Delta-G is represented as a 5-tuple of
      delta-G'<sup>0</sup>, temperature, ionic strength , pH, and pMg . A conversion
      in BioPAX may have multiple Delta-G values, representing different measurements
      for delta-G'<sup>0</sup> obtained under the different experimental conditions.

    
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
        self.rdf_type="http://www.biopax.org/release/biopax-level3.owl#DeltaG"
        self._deltaGPrime0=kwargs.get('deltaGPrime0',None)  
        self._ionicStrength=kwargs.get('ionicStrength',None)  
        self._ph=kwargs.get('ph',None)  
        self._pMg=kwargs.get('pMg',None)  
        self._temperature=kwargs.get('temperature',None)  
        self._comment=kwargs.get('comment',None)  
  

##########getter
     
    def get_deltaGPrime0(self):
        """
        Attribute _deltaGPrime0  getter
                      For biochemical reactions, this property refers to the standard transformed
      Gibbs energy change for a reaction written in terms of biochemical reactants
      (sums of species), delta-G'<sup>o</sup>.    delta-G'<sup>o</sup> = -RT lnK' and
      delta-G'<sup>o</sup> = delta-H'<sup>o</sup> - T delta-S'<sup>o</sup>
      delta-G'<sup>o</sup> has units of kJ/mol.  Like K', it is a function of
      temperature (T), ionic strength (I), pH, and pMg (pMg =
      -log<sub>10</sub>[Mg<sup>2+</sup>]). Therefore, these quantities must be
      specified, and values for DELTA-G for biochemical reactions are represented as
      5-tuples of the form (delta-G'<sup>o</sup> T I pH pMg).

                """
        return self._deltaGPrime0  
     
    def get_ionicStrength(self):
        """
        Attribute _ionicStrength  getter
                      The ionic strength is defined as half of the total sum of the concentration (ci)
      of every ionic species (i) in the solution times the square of its charge (zi).
      For example, the ionic strength of a 0.1 M solution of CaCl2 is 0.5 x (0.1 x 22
      + 0.2 x 12) = 0.3 M

                """
        return self._ionicStrength  
     
    def get_ph(self):
        """
        Attribute _ph  getter
                      A measure of acidity and alkalinity of a solution that is a number on a scale on
      which a value of 7 represents neutrality and lower numbers indicate increasing
      acidity and higher numbers increasing alkalinity and on which each unit of
      change represents a tenfold change in acidity or alkalinity and that is the
      negative logarithm of the effective hydrogen-ion concentration or hydrogen-ion
      activity in gram equivalents per liter of the solution. (Definition from
      Merriam-Webster Dictionary)

                """
        return self._ph  
     
    def get_pMg(self):
        """
        Attribute _pMg  getter
                      A measure of the concentration of magnesium (Mg) in solution. (pMg =
      -log<sub>10</sub>[Mg<sup>2+</sup>])

                """
        return self._pMg  
     
    def get_temperature(self):
        """
        Attribute _temperature  getter
                      Temperature in Celsius

                """
        return self._temperature  
     
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
    
    @validator(value="float", nullable=False)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  False
    def set_deltaGPrime0(self,value):
        self._deltaGPrime0=value  
    
    @validator(value="float", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_ionicStrength(self,value):
        self._ionicStrength=value  
    
    @validator(value="float", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_ph(self,value):
        self._ph=value  
    
    @validator(value="float", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_pMg(self,value):
        self._pMg=value  
    
    @validator(value="float", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_temperature(self,value):
        self._temperature=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_comment(self,value):
        self._comment=value  
  




    def object_attributes(self):

      object_attribute_list=super().object_attributes() 
      return object_attribute_list
 

    def type_attributes(self):
 
      type_attribute_list=super().type_attributes() 
      satt=['deltaGPrime0', 'ionicStrength', 'ph', 'pMg', 'temperature']
      for elem in satt:
        type_attribute_list.append(elem)
      return type_attribute_list
 
#####get attributes types 
    def attribute_type_by_name(self):
      ma=dict()
      ma=super().attribute_type_by_name() 
      ma['deltaGPrime0']='float'  
      ma['ionicStrength']='float'  
      ma['ph']='float'  
      ma['pMg']='float'  
      ma['temperature']='float'  
      ma['comment']='str'  
      return ma



    def to_json(self):
        return tojson(self)
        

    def get_uri_string(self):
        return self.pk

    def set_uri_string(self,uristr):
        self.pk= uristr       