 
from biopax.physicalentity import PhysicalEntity
##############################
 


 
from biopax.utils.class_utils import tostring,tojson
from biopax.utils.validate_utils import CValidateArgType,raise_error





validator = CValidateArgType(raise_error, logger=None)

@tostring
class Complex(PhysicalEntity) :


    """
    Class Complex 
    
        
          Definition: A physical entity whose structure is comprised of other physical
      entities bound to each other covalently or non-covalently, at least one of which
      is a macromolecule (e.g. protein, DNA, or RNA) and the Stoichiometry of the
      components are known.   Comment: Complexes must be stable enough to function as
      a biological unit; in general, the temporary association of an enzyme with its
      substrate(s) should not be considered or represented as a complex. A complex is
      the physical product of an interaction (complexAssembly) and is not itself
      considered an interaction. The boundaries on the size of complexes described by
      this class are not defined here, although possible, elements of the cell  such a
      mitochondria would typically not be described using this class (later versions
      of this ontology may include a cellularComponent class to represent these). The
      strength of binding cannot be described currently, but may be included in future
      versions of the ontology, depending on community need. Examples: Ribosome, RNA
      polymerase II. Other examples of this class include complexes of multiple
      protein monomers and complexes of proteins and small molecules.

    
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
        self.rdf_type="http://www.biopax.org/release/biopax-level3.owl#Complex"
        self._component=kwargs.get('component',None)  
        self._componentStoichiometry=kwargs.get('componentStoichiometry',None)  
        self._cellularLocation=kwargs.get('cellularLocation',None)  
        self._feature=kwargs.get('feature',None)  
        self._memberPhysicalEntity=kwargs.get('memberPhysicalEntity',None)  
        self._notFeature=kwargs.get('notFeature',None)  
  

##########getter
     
    def get_component(self):
        """
        Attribute _component  getter
                """
        return self._component  
     
    def get_componentStoichiometry(self):
        """
        Attribute _componentStoichiometry  getter
                      The stoichiometry of components in a complex

                """
        return self._componentStoichiometry  
     
    def get_cellularLocation(self):
        """
        Attribute _cellularLocation  getter
                      A cellular location, e.g. 'cytoplasm'. This should reference a term in the Gene
      Ontology Cellular Component ontology. The location referred to by this property
      should be as specific as is known. If an interaction is known to occur in
      multiple locations, separate interactions (and physicalEntities) must be created
      for each different location.  If the location of a participant in a complex is
      unspecified, it may be assumed to be the same location as that of the complex.
      A molecule in two different cellular locations are considered two different
      physical entities.

                """
        return self._cellularLocation  
     
    def get_feature(self):
        """
        Attribute _feature  getter
                      Sequence features of the owner physical entity.

                """
        return self._feature  
     
    def get_memberPhysicalEntity(self):
        """
        Attribute _memberPhysicalEntity  getter
                      This property stores the members of a generic physical entity.   For
      representing homology generics a better way is to use generic entity references
      and generic features. However not all generic logic can be captured by this,
      such as complex generics or rare cases where feature cardinality is variable.
      Usages of this property should be limited to such cases.

                """
        return self._memberPhysicalEntity  
     
    def get_notFeature(self):
        """
        Attribute _notFeature  getter
                      Sequence features where the owner physical entity has a feature. If not
      specified, other potential features are not known.

                """
        return self._notFeature  
  
##########setter
    
    @validator(value="biopax.PhysicalEntity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_component(self,value):
        self._component=value  
    
    @validator(value="biopax.Stoichiometry", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_componentStoichiometry(self,value):
        self._componentStoichiometry=value  
    
    @validator(value="biopax.CellularLocationVocabulary", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_cellularLocation(self,value):
        self._cellularLocation=value  
    
    @validator(value="biopax.EntityFeature", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_feature(self,value):
        self._feature=value  
    
    @validator(value="biopax.PhysicalEntity", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_memberPhysicalEntity(self,value):
        self._memberPhysicalEntity=value  
    
    @validator(value="biopax.EntityFeature", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_notFeature(self,value):
        self._notFeature=value  
  




    def object_attributes(self):

      object_attribute_list=super().object_attributes() 
      satt=['component', 'componentStoichiometry']
      for elem in satt:
        object_attribute_list.append(elem)
      return object_attribute_list
 

    def type_attributes(self):
 
      type_attribute_list=super().type_attributes() 
      return type_attribute_list
 
#####get attributes types 
    def attribute_type_by_name(self):
      ma=dict()
      ma=super().attribute_type_by_name() 
      ma['component']='PhysicalEntity'  
      ma['componentStoichiometry']='Stoichiometry'  
      ma['cellularLocation']='CellularLocationVocabulary'  
      ma['feature']='EntityFeature'  
      ma['memberPhysicalEntity']='PhysicalEntity'  
      ma['notFeature']='EntityFeature'  
      return ma



    def to_json(self):
        return tojson(self)
        

    def get_uri_string(self):
        return self.pk

    def set_uri_string(self,uristr):
        self.pk= uristr       