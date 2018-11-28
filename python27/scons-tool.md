### SCons Usage
## Summary
* scons is a automatic builder tool made by python, obvious advantages comparing with GNU make as below:
1. Protability: SCons can work where python can run
1. Expansibility: SCons only provide classes of python in theory, scons user can do all things which python can do.
1. Smart: SCons inherit features of autoconf/automake, will analyze system paths or typedef and so on automatically.

## SCons files
* posible files in scons: SConstruct/Sconstruct/sconstruct/SConscript
* scons will search config file in current path, according to the sequence SConstruct/Sconstruct/sconstruct, and read related config from first file.
* use SConscript() function to decide tributary config file in the SConstruct file. As usual, these tributary config files are named "SConscript", certainly, other names is ok.

## SCons command line parameter
* scons: execute SConstruct script
* scons -c: clean
* scons -Q: only display compiling info, remove needless printable info
* scons -Q --implicit-cache hello: save dependency
		   --implicit-deps-changed: force to update dependency
		   --implicit-deps-unchanged: force to use former dependency although changed
		   
## functions provided by SConstruct

* 1. Program: generate executable files
* Program('hello.c') compile hello.c and auto-generate executable file depending on system(hello.exe on windows; hello on Posix)
* Program('hello','hello.c') assign filename output
* Program(['hello.c','file1.c','file2.c']) when compiling multiple files, output filename will be named according to the first file
* Program(source = "hello.c",target = "hello")
* Program(target = "hello" , source = "hello.c")
* Program('hello', Split('hello.c file1.c file2.c')) compiling multiple files
* Program(Glob("*.c")); src = ["hello.c","foo.c"]; Program(src)

* 2. Object: generate target file
* Object('hello.c') compiling hello.c target file

* 3. Library：generate static or dynamic files
* Library('foo', ['f1.c', 'f2.c', 'f3.c']) compiling library
* SharedLibrary('foo', ['f1.c', 'f2.c', 'f3.c']) compiling shared library
* StaticLibrary('bar', ['f4.c', 'f5.c', 'f6.c']) compiling static library
* library usage：
* Program('prog.c', LIBS=['foo', 'bar'], LIBPATH='.') connect library, no need to add prefix or suffix

* 4. SourceSignatures：check if orignal file is changed
* SourceSignatures('MD5')     according if content is changed, default way
* SourceSignatures('timestamp') according modification time

* 5. TargetSignatures：判断目标文件是否改变
* TargetSignatures('build')   根据编译结果
* TargetSignatures('content')  根据文件内容，如果只是加了句注释，将不会被重新编译
 
* 6. Ignore：忽略依赖关系
* Ignore(hello, 'hello.h')  忽略某个依赖关系
 
* 7. Depends：明确依赖关系
* Depends(hello, 'other_file') 明确依赖关系

* 8. SConscript：scons的配置文件。
*  源文件的目录结构如下：
*   src：
*   |    SConstruct
*   |    test.cpp
*   |    mA(目录)：
*        |     SConscript
*        |     func.cpp
*   其中test.cpp为主文件，中调用func.cpp中定义的函数
*   SConstruct内容如下：
* subobj = SConscript(['mA/SConscript'])  
* obj = subobj + Object(Glob("*.cpp"))  
* Program("test",list(obj))  
*   SConscript内容 ：
* obj = Object(Glob("*.cpp"))  
* Return("obj")  
*上例中，在主目录中执行scons就可以编译整个"工程"。SConstruct编译主目录中的test.cpp，并通过SConscript编译mA目录下的源文件，
并最终生成可执行文件；SConscript用于编译mA中的func.cpp并把生成的func.o传递给主目录的SConstruct。

* 10. env：环境变量
*环境变量用于设置在编译过程中的各种参数，可以用下面的SConstruct打印环境变量的所有信息(实际上env就是一个python字典),可以使用如下的SConstruct查看环境变量的内容：
* env = Environment()  
* dict = env.Dictionary()  
* keys = dict.keys()  
* keys.sort()  
* for key in keys:  
*     print "construction variable = '%s', value = '%s'" % (key, dict[key])

