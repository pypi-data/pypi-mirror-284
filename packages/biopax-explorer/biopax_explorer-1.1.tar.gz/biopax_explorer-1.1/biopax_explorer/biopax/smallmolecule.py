 
from biopax.physicalentity import PhysicalEntity
##############################
 


 
from biopax.utils.class_utils import tostring,tojson
from biopax.utils.validate_utils import CValidateArgType,raise_error





validator = CValidateArgType(raise_error, logger=None)

@tostring
class SmallMolecule(PhysicalEntity) :


    """
    Class SmallMolecule 
    
        
          Definition: A pool of molecules that are neither complexes nor are genetically
      encoded.  Rationale: Identity of small molecules are based on structure, rather
      than sequence as in the case of DNA, RNA or Protein. A small molecule reference
      is a grouping of several small molecule entities  that have the same chemical
      structure.    Usage : Smalle Molecules can have a cellular location and binding
      features. They can't have modification features as covalent modifications of
      small molecules are not considered as state changes but treated as different
      molecules. Some non-genomic macromolecules, such as large complex carbohydrates
      are currently covered by small molecules despite they lack a static structure.
      Better coverage for such molecules require representation of generic
      stoichiometry and polymerization, currently planned for BioPAX level 4.
      Examples: glucose, penicillin, phosphatidylinositol

    
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
        self.rdf_type="http://www.biopax.org/release/biopax-level3.owl#SmallMolecule"
        self._entityReference=kwargs.get('entityReference',None)  
        self._cellularLocation=kwargs.get('cellularLocation',None)  
        self._feature=kwargs.get('feature',None)  
        self._memberPhysicalEntity=kwargs.get('memberPhysicalEntity',None)  
        self._notFeature=kwargs.get('notFeature',None)  
        self._cellularLocation=kwargs.get('cellularLocation',None)  
        self._feature=kwargs.get('feature',None)  
        self._memberPhysicalEntity=kwargs.get('memberPhysicalEntity',None)  
        self._notFeature=kwargs.get('notFeature',None)  
        self._cellularLocation=kwargs.get('cellularLocation',None)  
        self._feature=kwargs.get('feature',None)  
        self._memberPhysicalEntity=kwargs.get('memberPhysicalEntity',None)  
        self._notFeature=kwargs.get('notFeature',None)  
        self._cellularLocation=kwargs.get('cellularLocation',None)  
        self._feature=kwargs.get('feature',None)  
        self._memberPhysicalEntity=kwargs.get('memberPhysicalEntity',None)  
        self._notFeature=kwargs.get('notFeature',None)  
  

##########getter
     
    def get_entityReference(self):
        """
        Attribute _entityReference  getter
                      Reference entity for this physical entity.

                """
        return self._entityReference  
     
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
    
    @validator(value="biopax.EntityReference", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_entityReference(self,value):
        self._entityReference=value  
    
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
      satt=['entityReference']
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
      ma['entityReference']='EntityReference'  
      ma['cellularLocation']='CellularLocationVocabulary'  
      ma['feature']='EntityFeature'  
      ma['memberPhysicalEntity']='PhysicalEntity'  
      ma['notFeature']='EntityFeature'  
      ma['cellularLocation']='CellularLocationVocabulary'  
      ma['feature']='EntityFeature'  
      ma['memberPhysicalEntity']='PhysicalEntity'  
      ma['notFeature']='EntityFeature'  
      ma['cellularLocation']='CellularLocationVocabulary'  
      ma['feature']='EntityFeature'  
      ma['memberPhysicalEntity']='PhysicalEntity'  
      ma['notFeature']='EntityFeature'  
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