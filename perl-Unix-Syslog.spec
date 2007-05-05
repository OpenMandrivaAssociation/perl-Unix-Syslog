%define	module	Unix-Syslog
%define	name	perl-%{module}
%define	version	0.100
%define	release	%mkrel 4

Name:		%{name}
Summary:	Perl interface to the UNIX system logger
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://www.cpan.org/
Source0:	%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides access to the system logger available on most
UNIX systems via perl XSUBs (perl's C interface).

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%{perl_vendorarch}/*
%{_mandir}/*/*

