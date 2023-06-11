#include <stdio.h>
#include <time.h>
#include <sys/time.h>
#include <Python.h>
/**
  * print_python_list_info - print lists info
  *
  * @p: python object
  */
void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *it;

	for (i = 0; i < 2; i++)
	{
		it = PyList_GetItem(p, i);
		printf("%s\n", PyUnicode_AsUTF8(it));
	}
}
