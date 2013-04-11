%define libname %mklibname %{name}
%define libnamedev %{libname}-devel

Summary: SCEW provides an easy interface around the XML Expat library
Name:    scew
Version: 0.4.0
Release: 2
Source0: %{name}-%{version}.tar.bz2
License: LGPL
Group: Development/C
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
%configure --includedir=%{_includedir}/%{name}
%make 

%install
%makeinstall_std

mkdir -p %{buildroot}%{_bindir}
install -m 755 examples/scew_print/scew_print %{buildroot}%{_bindir}
install -m 755 examples/scew_write/scew_write %{buildroot}%{_bindir}

%files -n %libnamedev
%defattr(-,root,root,0755)
%{_bindir}/scew_print
%{_bindir}/scew_write
%{_libdir}/libscew.a
%{_includedir}/*
%_libdir/pkgconfig/*



%changelog
* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.4.0-1mdv2008.1
+ Revision: 126978
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import scew


* Thu Jan 13 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.4.0-1mdk
- 0.4.0

* Sat Dec 13 2003 Franck Villaume <fvill@freesurf.fr> 0.3.1-2mdk
- add BuildRequires : expat-devel
- use mklibname macro

* Fri Oct 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-1mdk
- from Jan Villat <rpms@djdie.net> : 
	- First RPM build

# end of file
