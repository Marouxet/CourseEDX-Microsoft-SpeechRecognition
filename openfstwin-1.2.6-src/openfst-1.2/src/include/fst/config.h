#define HAVE_STD__TR1__HASH_LONG_LONG_UNSIGNED_ 1

#ifdef _WIN32 
#pragma warning(disable:4018 4244 4996 4099 4503 4800 4305 4355 4396 4715 4180 4244 4224)
#define HAVE_STD__TR1__HASH_LONG_LONG_UNSIGNED_ 1
#define WINDOWS 1
#define WIN32_LEAN_AND_MEAN
#else
#undef WINDOWS
#endif
