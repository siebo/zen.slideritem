"""Definition of the Slider Item content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

# -*- Message Factory Imported Here -*-

from zen.slideritem.interfaces import ISliderItem
from zen.slideritem.config import PROJECTNAME

SliderItemSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.StringField('tabTitle',
              searchable=0,
              widget=atapi.StringWidget(label="Tab title")
              ),

    atapi.ImageField('image',
               sizes= {'large'   : (639, 335),},
               widget = atapi.ImageWidget(
                        label= "Slider Image",
                        description = "",
                        show_content_type = False,)
               ),

    atapi.BooleanField('useImage',
              searchable=0,
              widget=atapi.BooleanWidget(label="Use Image",
                                         description = "Use image instead of text for inner content",
                                         )
              ),

    atapi.ImageField('innerimage',
               sizes= {'large'   : (389, 145),},
               widget = atapi.ImageWidget(
                        label= "Inner Image",
                        description = "",
                        show_content_type = False,)
               ),

    atapi.ReferenceField('linkTarget',
              searchable=0,
              relationship='link_target',
              widget=ReferenceBrowserWidget(label="Link Target")
              ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

SliderItemSchema['title'].storage = atapi.AnnotationStorage()
SliderItemSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(SliderItemSchema, moveDiscussion=False)


class SliderItem(base.ATCTContent):
    """Slider Item content-type"""
    implements(ISliderItem)

    meta_type = "SliderItem"
    schema = SliderItemSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(SliderItem, PROJECTNAME)
