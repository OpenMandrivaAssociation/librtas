%define name	librtas
%define version	1.2.4
%define release	%mkrel 3

%define libname	%mklibname rtas 1

Summary:	Libraries for user-space access to the Run-Time Abstraction Services (RTAS)
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	IBM Common Public License
Group:		System/Libraries
Url:		http://librtas.ozlabs.org/
ExclusiveArch:	ppc ppc64
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The librtas shared library provides userspace with an interface
through which certain RTAS calls can be made.  The library uses either
of the RTAS User Module or the RTAS system call to direct the kernel
in making these calls.

The librtasevent shared library provides users with a set of
definitions and common routines useful in parsing and dumping the
contents of RTAS events.

%package -n %{libname}
Summary:	Runtime libraries for user-space access to RTAS
Group:		System/Libraries

%description -n %{libname}
Librtas provides a set of libraries for user-space access to the
Run-Time Abstraction Services (RTAS) on PowerPC architectures.

%package -n %{libname}-devel
Summary:	Libraries and include files for developing with librtas
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n %{libname}-devel
This package provides the necessary development libraries and include
files to allow you to develop with librtas.

%prep
%setup -q
perl -pi -e "s|^(LIB_DIR\s+=\s+).+$|\1%{_libdir}|" rules.mk

%build
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig 
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc README COPYRIGHT
%{_libdir}/librtas.so.*
%{_libdir}/librtasevent.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc README COPYRIGHT
%{_includedir}/librtas*.h
%{_libdir}/librtas.a
%{_libdir}/librtas.so
%{_libdir}/librtasevent.so

