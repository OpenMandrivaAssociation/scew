%define name scew
%define version 1.1.0
%define release %mkrel 1

%define major 1
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d
%define libnamedevstatic %mklibname %{name} -d -s

Summary: SCEW provides an easy interface around the XML Expat library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://savannah.nongnu.org/download/scew/%{name}-%{version}.tar.gz
License: LGPLv2+
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

%package -n %{libname}
Summary: Scew shared library
Group: System/Libraries
Provides: lib%{name} = %{version}-%{release}

%description -n %{libname}
SCEW (Simple C Expat Wrapper) incorporated functions to create XML
files and handle XML memory trees. That is, add and delete tree nodes,
change attribute names and values...

SCEW provides functions to load and access XML elements without the
need to create the event handling routines and probably the most
important: without the need to rewrite these functions each time you
need to load a different XML tree. It also lets you access to the
internal Expat parser, that means you can still have all the
functionality that Expat library gives you.

This package contains the scew shared library.

%package -n %{libnamedev}
Summary: Headers for developing programs that will use scew
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
This package contains the headers that programmers will need to develop
applications which will use scew.

%package -n %{libnamedevstatic}
Summary: Static development file for %{name}
Group: Development/C
Requires: %{libnamedev} = %{version}-%{release}
Provides: %{name}-static-devel = %{version}-%{release}

%description -n %{libnamedevstatic}
This package contains the static development file for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make 

%install
rm -rf %{buildroot}
%makeinstall

mkdir -p %{buildroot}%{_bindir}
install -m 755 examples/scew_print/scew_print %{buildroot}%{_bindir}/
install -m 755 examples/scew_write/scew_write %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so.*

%files -n %{libnamedev}
%defattr(-,root,root,0755)
%{_bindir}/%{name}_print
%{_bindir}/%{name}_write
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.la
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files -n %{libnamedevstatic}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.a

