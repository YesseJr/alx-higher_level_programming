/*
 * Project - 0x03-python-data_structures
 * File - 100-print_python_list_info.c
 * Author - Waython Yesse
 * Occupation - Software Engineering Student at ALX
 * Year - 2021 November 21
 */

#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, idx;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (idx = 0; idx < size; idx++)
	{
		printf("Element %ld: %s\n",
		       idx,
		       (PY_TYPE(PyList_GetItem(p, idx)))->tp_name);
	}
}
