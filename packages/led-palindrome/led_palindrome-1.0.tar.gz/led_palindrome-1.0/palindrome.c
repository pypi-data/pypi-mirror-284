#include <Python.h>

static PyObject *is_palindrome(PyObject *self, PyObject *args) {
    int i, n;
    const char *text;
    int result;
    if (!PyArg_ParseTuple(args, "s", &text)) {
        return NULL;
    }
    n = strlen(text);
    result = 1;
    for (i = 0; i <= n/2; ++i) {
        if (text[i] != text[n-i-1]) {
            result = 0;
            break;
        }
    }
    return Py_BuildValue("i", result);
}

/* 方法列表 */
static PyMethodDef PalindromeMethods[] = {

    /* 名称, 函数, 参数类型, 文档字符串 */
    {"is_palindrome", is_palindrome, METH_VARARGS, "Detect palindromes"},
    {NULL, NULL, 0, NULL}

};

/* 模块列表 */
static struct PyModuleDef palindrome =
{
    PyModuleDef_HEAD_INIT,
    "led_palindrome", /* module name */
    "i am desc of mode",           /* docstring */
    -1,           /* signals state kept in global variables */
    PalindromeMethods
};


/* 模块初始化函数 */
PyMODINIT_FUNC PyInit_led_palindrome(void)
{
    return PyModule_Create(&palindrome);
}