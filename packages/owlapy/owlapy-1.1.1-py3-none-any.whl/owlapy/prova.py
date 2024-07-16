from owlapy.class_expression import OWLClass, OWLObjectSomeValuesFrom
from owlapy.iri import IRI
from owlapy.owl_property import OWLObjectProperty

namespace = "http://example.com/family#"
person = OWLClass(IRI(namespace, "Grandmother"))
hasChild = OWLObjectProperty("http://example.com/family#hasChild")
sm = OWLObjectSomeValuesFrom(hasChild.get_inverse_property(), person)

print(sm)

