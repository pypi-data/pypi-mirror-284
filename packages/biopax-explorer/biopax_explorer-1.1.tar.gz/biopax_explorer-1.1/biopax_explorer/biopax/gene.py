 
from biopax.entity import Entity
##############################
 


 
from biopax.utils.class_utils import tostring,tojson
from biopax.utils.validate_utils import CValidateArgType,raise_error





validator = CValidateArgType(raise_error, logger=None)

@tostring
class Gene(Entity) :


    """
    Class Gene 
    
        
          Definition: A continuant that encodes information that can be inherited through
      replication.  Rationale: Gene is an abstract continuant that can be best
      described as a "schema", a common conception commonly used by biologists to
      demark a component within genome. In BioPAX, Gene is considered a generalization
      over eukaryotic and prokaryotic genes and is used only in genetic interactions.
      Gene is often confused with DNA and RNA fragments, however, these are considered
      the physical encoding of a gene.  N.B. Gene expression regulation makes use of
      DNA and RNA physical entities and not this class. Usage: Gene should only be
      used for describing GeneticInteractions.

    
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
        self.rdf_type="http://www.biopax.org/release/biopax-level3.owl#Gene"
        self._organism=kwargs.get('organism',None)  
        self._dataSource=kwargs.get('dataSource',None)  
        self._evidence=kwargs.get('evidence',None)  
        self._xref=kwargs.get('xref',None)  
        self._availability=kwargs.get('availability',None)  
        self._comment=kwargs.get('comment',None)  
        self._displayName=kwargs.get('displayName',None)  
        self._name=kwargs.get('name',None)  
        self._standardName=kwargs.get('standardName',None)  
  

##########getter
     
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
     
    def get_dataSource(self):
        """
        Attribute _dataSource  getter
                      A free text description of the source of this data, e.g. a database or person
      name. This property should be used to describe the source of the data. This is
      meant to be used by databases that export their data to the BioPAX format or by
      systems that are integrating data from multiple sources. The granularity of use
      (specifying the data source in many or few instances) is up to the user. It is
      intended that this property report the last data source, not all data sources
      that the data has passed through from creation.

                """
        return self._dataSource  
     
    def get_evidence(self):
        """
        Attribute _evidence  getter
                      Scientific evidence supporting the existence of the entity as described.

                """
        return self._evidence  
     
    def get_xref(self):
        """
        Attribute _xref  getter
                      Values of this property define external cross-references from this entity to
      entities in external databases.

                """
        return self._xref  
     
    def get_availability(self):
        """
        Attribute _availability  getter
                      Describes the availability of this data (e.g. a copyright statement).

                """
        return self._availability  
     
    def get_comment(self):
        """
        Attribute _comment  getter
                      Comment on the data in the container class. This property should be used instead
      of the OWL documentation elements (rdfs:comment) for instances because
      information in 'comment' is data to be exchanged, whereas the rdfs:comment field
      is used for metadata about the structure of the BioPAX ontology.

                """
        return self._comment  
     
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
    
    @validator(value="biopax.BioSource", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  1
           #att.nullable:  True
    def set_organism(self,value):
        self._organism=value  
    
    @validator(value="biopax.Provenance", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_dataSource(self,value):
        self._dataSource=value  
    
    @validator(value="biopax.Evidence", nullable=True)
           #att.list:   False
           #att.min:   None
           #att.max :  None
           #att.nullable:  True
    def set_evidence(self,value):
        self._evidence=value  
    
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
    def set_availability(self,value):
        self._availability=value  
    
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
      satt=['organism']
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
      ma['organism']='BioSource'  
      ma['dataSource']='Provenance'  
      ma['evidence']='Evidence'  
      ma['xref']='Xref'  
      ma['availability']='str'  
      ma['comment']='str'  
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