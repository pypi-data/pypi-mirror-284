/* Generated by Cython 3.0.10 */

#ifndef __PYX_HAVE__xtrack__xmad__xmad
#define __PYX_HAVE__xtrack__xmad__xmad

#include "Python.h"

#ifndef __PYX_HAVE_API__xtrack__xmad__xmad

#ifdef CYTHON_EXTERN_C
    #undef __PYX_EXTERN_C
    #define __PYX_EXTERN_C CYTHON_EXTERN_C
#elif defined(__PYX_EXTERN_C)
    #ifdef _MSC_VER
    #pragma message ("Please do not define the '__PYX_EXTERN_C' macro externally. Use 'CYTHON_EXTERN_C' instead.")
    #else
    #warning Please do not define the '__PYX_EXTERN_C' macro externally. Use 'CYTHON_EXTERN_C' instead.
    #endif
#else
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#ifndef DL_IMPORT
  #define DL_IMPORT(_T) _T
#endif

__PYX_EXTERN_C void yyerror(YYLTYPE *, yyscan_t, char const *);
__PYX_EXTERN_C PyObject *py_integer(yyscan_t, long);
__PYX_EXTERN_C PyObject *py_float(yyscan_t, double);
__PYX_EXTERN_C PyObject *py_unary_op(yyscan_t, char const *, PyObject *);
__PYX_EXTERN_C PyObject *py_binary_op(yyscan_t, char const *, PyObject *, PyObject *);
__PYX_EXTERN_C PyObject *py_eq_value_scalar(yyscan_t, char const *, PyObject *);
__PYX_EXTERN_C PyObject *py_eq_defer_scalar(yyscan_t, char const *, PyObject *);
__PYX_EXTERN_C PyObject *py_call_func(yyscan_t, char const *, PyObject *);
__PYX_EXTERN_C PyObject *py_arrow(yyscan_t, char const *, char const *);
__PYX_EXTERN_C PyObject *py_identifier_atom(yyscan_t, char const *);
__PYX_EXTERN_C void py_set_defer(yyscan_t, PyObject *);
__PYX_EXTERN_C void py_set_value(yyscan_t, PyObject *);
__PYX_EXTERN_C void py_make_sequence(yyscan_t, char const *, PyObject *, PyObject *);
__PYX_EXTERN_C PyObject *py_clone(yyscan_t, char const *, char const *, PyObject *);
__PYX_EXTERN_C PyObject *py_eq_value_sum(yyscan_t, char const *, PyObject *);
__PYX_EXTERN_C PyObject *py_eq_defer_sum(yyscan_t, char const *, PyObject *);
__PYX_EXTERN_C PyObject *py_eq_value_array(yyscan_t, char const *, PyObject *);
__PYX_EXTERN_C PyObject *py_eq_defer_array(yyscan_t, char const *, PyObject *);
__PYX_EXTERN_C PyObject *__pyx_fuse_0py_numeric(yyscan_t, double);
__PYX_EXTERN_C PyObject *__pyx_fuse_1py_numeric(yyscan_t, long);

#endif /* !__PYX_HAVE_API__xtrack__xmad__xmad */

/* WARNING: the interface of the module init function changed in CPython 3.5. */
/* It now returns a PyModuleDef instance instead of a PyModule instance. */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initxmad(void);
#else
/* WARNING: Use PyImport_AppendInittab("xmad", PyInit_xmad) instead of calling PyInit_xmad directly from Python 3.5 */
PyMODINIT_FUNC PyInit_xmad(void);

#if PY_VERSION_HEX >= 0x03050000 && (defined(__GNUC__) || defined(__clang__) || defined(_MSC_VER) || (defined(__cplusplus) && __cplusplus >= 201402L))
#if defined(__cplusplus) && __cplusplus >= 201402L
[[deprecated("Use PyImport_AppendInittab(\"xmad\", PyInit_xmad) instead of calling PyInit_xmad directly.")]] inline
#elif defined(__GNUC__) || defined(__clang__)
__attribute__ ((__deprecated__("Use PyImport_AppendInittab(\"xmad\", PyInit_xmad) instead of calling PyInit_xmad directly."), __unused__)) __inline__
#elif defined(_MSC_VER)
__declspec(deprecated("Use PyImport_AppendInittab(\"xmad\", PyInit_xmad) instead of calling PyInit_xmad directly.")) __inline
#endif
static PyObject* __PYX_WARN_IF_PyInit_xmad_INIT_CALLED(PyObject* res) {
  return res;
}
#define PyInit_xmad() __PYX_WARN_IF_PyInit_xmad_INIT_CALLED(PyInit_xmad())
#endif
#endif

#endif /* !__PYX_HAVE__xtrack__xmad__xmad */
