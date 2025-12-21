%define	module	Unix-Syslog

Summary:	Perl interface to the UNIX system logger
Name:		perl-%{module}
Version:	1.1
Release:	2
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/Unix::Syslog
Source0:	http://www.cpan.org/modules/by-module/Unix/%{module}-%{version}.tar.gz
BuildRequires:	make
Buildrequires:	perl-devel

%description
This module provides access to the system logger available on most
UNIX systems via perl XSUBs (perl's C interface).

%prep
%autosetup -p1 -n %{module}-%{version}

%build
CFLAGS="%{optflags}" %__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorarch}/*
%{_mandir}/man3/*
