@echo off
REM grap2graph -- compile graph description descriptions to bitmap images
REM
REM by Eli Zaretskii <eliz@gnu.org>, translation of a Unix shell
REM script written by Eric S. Raymond <esr@thyrsus.com>, May 2003
REM
REM In Unixland, the magic is in knowing what to string together...
REM
REM Take grap description on stdin, emit cropped bitmap on stdout.
REM The pic markup should *not* be wrapped in .G1/.G2, this script will do that.
REM A -U option on the command line enables gpic/groff "unsafe" mode.
REM A -format FOO option changes the image output format to any format
REM supported by convert(1).  All other options are passed to convert(1).
REM The default format is PNG.
REM
REM
REM Requires the groff suite and the ImageMagick tools.  Both are open source.
REM This code is released to the public domain.
REM
REM Here are the assumptions behind the option processing:
REM
REM 1. None of the options of grap(1) are relevant.
REM
REM 2. Only the -U option of groff(1) is relevant.
REM
REM 3. Many options of convert(1) are potentially relevant, (especially 
REM -density, -interlace, -transparency, -border, and -comment).
REM
REM Thus, we pass -U to groff(1), and everything else to convert(1).
REM
setlocal
set groff_opts=
set convert_opts=
set format=png

:loop
if "%1" == "" goto body
if "%1" == "-v" goto version
if "%1" == "--version" goto version
if "%1" == "--help" goto usage
if not "%1%" == "-unsafe" goto format
set groff_opts=-U
shift
goto loop
:format
if not "%1" == "-format" goto convert
set format=%2
shift
shift
goto loop
:convert
set convert_opts=%convert_opts% %1
shift
goto loop

:body
REM echo %groff_opts% %convert_opts% %format%

set rnd1=%RANDOM%
set rnd2=%RANDOM%
if "%GROFF_TMPDIR%" == "" goto deftmp
set tdir=%GROFF_TMPDIR%\grap2graph-%rnd1%
goto runpipe
:deftmp
sei tdir=%TEMP%\grap2graph-%rnd1%

:runpipe
mkdir %tdir%
echo .G1 > %tdir%\wrap
cat >> %tdir%\wrap
echo .G2 >> %tdir%\wrap
grap %tdir%\wrap | groff -p %groff_opts% -Tps -P-pletter | convert -trim -crop 0x0 %convert_opts% - %tdir%/grap2graph.%format%
cat %tdir%/grap2graph.%format%
rm -rf %tdir%
goto end

:version
echo GNU grap2graph (groff) version 1.22.4
goto end

:usage
echo usage: grap2graph ^[ option ...^] ^< in ^> out
echo.

:end
endlocal
