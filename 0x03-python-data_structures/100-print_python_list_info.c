#include <Python.h>

/**
* print_python_list_info - gives information for lists in python
* @p: the required list
*/
void print_python_list_info(PyObject *p)
{
int s, reserve, idx;
PyObject *p2;
s = Py_SIZE(p);
reserve = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %d\n", s);
printf("[*] Allocated = %d\n", reserve);
for (idx = 0; idx < s; idx++)
{
printf("Element %d: ", idx);
p2 = PyList_GetItem(p, idx);
printf("%s\n", Py_TYPE(p2)->tp_name);
}
}
