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

* 环境变量的使用：
* 	env = Environment()   #创建默认的环境变量，默认scons会按编译器的默认选项来进行编译
* 	import os
* 	env = Environment(CC = 'gcc',CCFLAGS = '-O2') #创建并设置环境 变量
* 	env.Program('foo.c') 

* 环境变量的复制：
*  	env = Environment(CC = 'gcc')
*  	opt = env.Clone(CCFLAGS = '-O2')
*  	dbg = env.Clone(CCFLAGS = '-g')
* 环境变量的替换：
*  	env = Environment(CCFLAGS = '-DDEFINE1')
*  	env.Replace(CCFLAGS = '-DDEFINE2')
*  	env.Program('foo.c') 
* 环境变量的输入输出：用于统一多目录源文件的编译选项，如：
*	src：
*	|    SConstruct
*	|    libstlport.a
*	|    test.cpp
*	|     include(目录)：
*	  |    foo.h
*	|    mA(目录)：
*	  |    SConscript
*	  |    func.cpp
*	
*	
* test.cpp和mA/func.cpp都引用了include/foo.h,test.cpp调用了mA/func.cpp的功能函数，其中include/foo.h中
定义了一个包含string类型的类。

* SConstruct如下：
* env = Environment()  
* flags = env.ParseFlags(['-pthread -I/usr/include/stlport ',' -L .'])  
* env.MergeFlags(class_flags)  
* subobj = SConscript(['mA/SConscript'])  
* obj = subobj + env.Object(Glob("*.cpp"))  
* env.Program("test",list(obj),LIBS = ['libstlport.a']) 

* mA/SConscrip如下:
* obj = Object(Glob("*.cpp"))  
* Return("obj")  

* 不出意外的话上边的工程编译可以通过，但是运行的时候会Aborted。因为test.cpp,mA/func.cpp都使用了包含string类型的那个类，
但是由于编译环境的不同，test.cpp认为string变量的大小是24字节, mA/func.cpp认为string变量的大小是4个字节(libstlport.a捣的鬼)。
     
* 解决问题的办法就是环境变量输出，修改SConstruct和mA/SConscript如下：
* SConstruct：
* env = Environment()  
* flags = env.ParseFlags(['-pthread -I/usr/include/stlport ',' -L .'])  
* env.MergeFlags(class_flags)  
* Export('env')  
* subobj = SConscript(['mA/SConscript'],exports = 'env')  
* obj = subobj + env.Object(Glob("*.cpp"))  
* env.Program("test",list(obj),LIBS = ['libstlport.a']) 

* mA/SConscript:
* Import('env')  
* obj = env.Object(Glob("*.cpp"))  
* Return("obj") 

### Detail information, Refer to this web site: https://scons.org/doc/2.1.0/