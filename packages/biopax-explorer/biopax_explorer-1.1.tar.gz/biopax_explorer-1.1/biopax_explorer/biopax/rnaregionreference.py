 
from biopax.entityreference import EntityReference
##############################
 


 
from biopax.utils.class_utils import tostring,tojson
from biopax.utils.validate_utils import CValidateArgType,raise_error





validator = CValidateArgType(raise_error, logger=None)

@tostring
class RnaRegionReference(EntityReference) :


    """
    Class RnaRegionReference 
    
        
          Definition: A RNARegion reference is a grouping of several RNARegion entities
      that are common in sequence and genomic position.  Members can differ in celular
      location, sequence features, mutations and bound partners.

    
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
        self.rdf_type="http://www.biopax.org/release/biopax-level3.owl#RnaRegionReference"
        self._absoluteRegion=kwargs.get('absoluteRegion',None)  
        self._organism=kwargs.get('organism',None)  
        self._regionType=kwargs.get('regionType',None)  
        self._subRegion=kwargs.get('subRegion',None)  
        self._sequence=kwargs.get('sequence',None)  
        self._entityFeature=kwargs.get('entityFeature',None)  
        self._entityReferenceType=kwargs.get('entityReferenceType',None)  
        self._evidence=kwargs.get('evidence',None)  
        self._memberEntityReference=kwargs.get('memberEntityReference',None)  
        self._xref=kwargs.get('xref',None)  
        self._displayName=kwargs.get('displayName',None)  
        self._name=kwargs.get('name',None)  
        self._standardName=kwargs.get('standardName',None)  
  

##########getter
     
    def get_absoluteRegion(self):
        """
        Attribute _absoluteRegion  getter
                      Absolute location as defined by the referenced sequence database record. E.g. an
      operon has a absolute region on the DNA molecule referenced by the
      UnificationXref.

                """
        return self._absoluteRegion  
     
    def get_organism(self):
        """
        Attribute _organism  getter
                      An organism, e.g. 'Homo sapiens'. This is the organism that the entity is found
      in. Pathways may not have an organism associated with them, for instance,
      reference pathways from KEGG. Sequence-based entities (DNA, protein, RNA) may
      contain an xref to a sequence database that contains organism information, in
      which case the information should be consistent with the value for ORGANISM.

                """
        return self._organism  
     
    def get_regionType(self):
        """
        Attribute _regionType  getter
                """
        return self._regionType  
     
    def get_subRegion(self):
        """
        Attribute _subRegion  getter
                      The sub region of a region or nucleic acid molecule. The sub region must be
      wholly part of the region, not outside of it.

                """
        return self._subRegion  
     
    def get_sequence(self):
        """
        Attribute _sequence  getter
                      Polymer sequence in uppercase letters. For DNA, usually A,C,G,T letters
      representing the nucleosides of adenine, cytosine, guanine and thymine,
      respectively; for RNA, usually A, C, U, G; for protein, usually the letters
      corresponding to the 20 letter IUPAC amino acid code.

                """
        return self._sequence  
     
    def get_entityFeature(self):
        """
        Attribute _entityFeature  getter
                      Variable features that are observed for the entities of this entityReference -
      such as known PTM or methylation sites and non-covalent bonds. Note that this is
      an aggregate list of all known features and it does not represent a state
      itself.

                """
        return self._entityFeature  
     
    def get_entityReferenceType(self):
        """
        Attribute _entityReferenceType  getter
                      A controlled vocabulary term that is used to describe the type of grouping such
      as homology or functional group.

                """
        return self._entityReferenceType  
     
    def get_evidence(self):
        """
        Attribute _evidence  getter
                      Scientific evidence supporting the existence of the entity as described.

                """
        return self._evidence  
     
    def get_memberEntityReference(self):
        """
        Attribute _memberEntityReference  getter
                      An entity reference that qualifies for the definition of this group. For example
      a member of a PFAM protein family.

                """
        return self._memberEntityReference  
     
    def get_xref(self):
        """
        Attribute _xref  getter
                      Values of this property define external cross-references from this entity to
      entities in external databases.

                """
        return self._xref  
     
    def get_displayName(self):
        """
        Attribute _displayName  getter
                      An abbreviated name for this entity, preferably a name that is short enough to
      be used in a visualization application to label a graphical element that
      represents this entity. If no short name is available, an xref may be used for
      this purpose by the visualization application.  Warning:  Subproperties of name
      are functional, that is we expect to have only one standardName and shortName
      for a given entity. If a user decides to assign a different name to standardName
      or shortName, they have to remove the old triplet from the model too. If the old
      name should be retained as a synonym a regular "name" property should also be
      introduced with the old name.

                """
        return self._displayName  
     
    def get_name(self):
        """
        Attribute _name  getter
                      Synonyms for this entity.  standardName and shortName are subproperties of this
      property and if declared they are automatically considered as names.   Warning:
      Subproperties of name are functional, that is we expect to have only one
      standardName and shortName for a given entity. If a user decides to assign a
      different name to standardName or shortName, they have to remove the old triplet
      from the model too. If the old name should be retained as a synonym a regular
      "name" property should also be introduced with the old name.

                """
        return self._name  
     
    def get_standardName(self):
        """
        Attribute _standardName  getter
                      The preferred full name for this entity, if exists assigned by a standard
      nomenclature organization such as HUGO Gene Nomenclature Committee.  Warning:
      Subproperties of name are functional, that is we expect to have only one
      standardName and shortName for a given entity. If a user decides to assign a
      different name to standardName or shortName, they have to remove the old triplet
      from the model too. If the old name should be retained as a synonym a regular
      "name" property should also be introduced with the old name.

                """
        return self._standardName  
  
##########setter
    
    @validator(value="biopax.SequenceLocation", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_absoluteRegion(self,value):
        self._absoluteRegion=value  
    
    @validator(value="biopax.BioSource", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_organism(self,value):
        self._organism=value  
    
    @validator(value="biopax.SequenceRegionVocabulary", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_regionType(self,value):
        self._regionType=value  
    
    @validator(value="biopax.DnaRegionReference", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_subRegion(self,value):
        self._subRegion=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_sequence(self,value):
        self._sequence=value  
    
    @validator(value="biopax.EntityFeature", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_entityFeature(self,value):
        self._entityFeature=value  
    
    @validator(value="biopax.EntityReferenceTypeVocabulary", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_entityReferenceType(self,value):
        self._entityReferenceType=value  
    
    @validator(value="biopax.Evidence", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_evidence(self,value):
        self._evidence=value  
    
    @validator(value="biopax.EntityReference", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_memberEntityReference(self,value):
        self._memberEntityReference=value  
    
    @validator(value="biopax.Xref", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_xref(self,value):
        self._xref=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_displayName(self,value):
        self._displayName=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_name(self,value):
        self._name=value  
    
    @validator(value="str", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_standardName(self,value):
        self._standardName=value  
  




    def object_attributes(self):

      object_attribute_list=super().object_attributes() 
      satt=['absoluteRegion', 'organism', 'regionType', 'subRegion']
      for elem in satt:
        object_attribute_list.append(elem)
      return object_attribute_list
 

    def type_attributes(self):
 
      type_attribute_list=super().type_attributes() 
      satt=['sequence']
      for elem in satt:
        type_attribute_list.append(elem)
      return type_attribute_list
 
#####get attributes types 
    def attribute_type_by_name(self):
      ma=dict()
      ma=super().attribute_type_by_name() 
      ma['absoluteRegion']='SequenceLocation'  
      ma['organism']='BioSource'  
      ma['regionType']='SequenceRegionVocabulary'  
      ma['subRegion']='DnaRegionReference'  
      ma['sequence']='str'  
      ma['entityFeature']='EntityFeature'  
      ma['entityReferenceType']='EntityReferenceTypeVocabulary'  
      ma['evidence']='Evidence'  
      ma['memberEntityReference']='EntityReference'  
      ma['xref']='Xref'  
      ma['displayName']='str'  
      ma['name']='str'  
      ma['standardName']='str'  
      return ma



    def to_json(self):
        return tojson(self)
        

    def get_uri_string(self):
        return self.pk

    def set_uri_string(self,uristr):
        self.pk= uristr       