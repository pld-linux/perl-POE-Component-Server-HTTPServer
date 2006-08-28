#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Server-HTTPServer
Summary:	perl(POE::Component::Server::HTTPServer) - serve HTTP requests
Name:		perl-POE-Component-Server-HTTPServer
Version:	0.9.2
Release:	0.1
# "same as perl"
License:	GPLv1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	766c06301099868fca4bbc8bd5cb358d
URL:		http://search.cpan.org/dist/%{pdir}-%{pnam}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
#BuildRequires:	-
%if %{with autodeps} || %{with tests}
#BuildRequires:	perl-
#BuildRequires:	perl-
%endif
#Requires:	-
#Provides:	-
#Obsoletes:	-
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module POE::Component::Server::HTTPServer is a POE based HTTP server.
Requests are dispatched based on an ordered list of "prefix => handler"
pairs.
This module was inspired by POE::Component::Server::HTTP, which deals with
request processing in a slightly different manner.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/Server/HTTPServer.pm
%dir %{perl_vendorlib}/POE/Component/Server/HTTPServer
%{perl_vendorlib}/POE/Component/Server/HTTPServer/*.pm
%{_mandir}/man3/*
