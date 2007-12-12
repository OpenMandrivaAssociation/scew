%define name scew
%define version 0.4.0
%define release 1mdk

%define libname %mklibname %{name}
#%define libname lib%{name}
%define libnamedev %{libname}-devel


Summary: SCEW provides an easy interface around the XML Expat library.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: LGPL
Group: Development/C
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: expat-devel
URL: http://www.nongnu.org/scew/

%description 
SCEW (Simple C Expat Wrapper) incorporated functions to create XML
files and handle XML memory trees. That is, add and delete tree nodes,
change attribute names and values...

SCEW provides functions to load and access XML elements without the
need to create the event handling routines and probably the most
important: without the need to rewrite these functions each time you
need to load a different XML tree. It also lets you access to the
internal Expat parser, that means you can still have all the
functionality that Expat library gives you.

%package -n %libnamedev
Summary: Headers for developing programs that will use scew
Group: Development/C
Provides:  libscew-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %libnamedev
This package contains the headers that programmers will need to develop
applications which will use scew.

%prep
%setup -q

%build
%configure
%make 

%install
%makeinstall

mkdir -p $RPM_BUILD_ROOT%_bindir
install -m 755 examples/scew_print/scew_print $RPM_BUILD_ROOT%_bindir/
install -m 755 examples/scew_write/scew_write $RPM_BUILD_ROOT%_bindir/

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libnamedev
%defattr(-,root,root,0755)
%{_bindir}/scew_print
%{_bindir}/scew_write
%{_libdir}/libscew.a
%{_includedir}/*
%_libdir/pkgconfig/*

