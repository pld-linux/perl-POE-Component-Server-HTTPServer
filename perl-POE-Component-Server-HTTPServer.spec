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
Release:	0.2
# "same as perl"
License:	GPLv1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	766c06301099868fca4bbc8bd5cb358d
URL:		http://search.cpan.org/dist/%{pdir}-%{pnam}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-MIME-Types
BuildRequires:	perl-POE
%endif
#Requires:	-
#Provides:	-
#Obsoletes:	-
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module POE::Component::Server::HTTPServer is a POE based HTTP
server. Requests are dispatched based on an ordered list of "prefix =>
handler" pairs. This module was inspired by
POE::Component::Server::HTTP, which deals with request processing in a
slightly different manner.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
pod2man --section 3 blib/lib/POE/Component/Server/HTTPServer/Examples.pod blib/man3/POE::Component::Server::HTTPServer::Examples.3pm

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/POE/Component/Server/HTTPServer/Examples.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/Server/HTTPServer.pm
%dir %{perl_vendorlib}/POE/Component/Server/HTTPServer
%{perl_vendorlib}/POE/Component/Server/HTTPServer/*.pm
%{_mandir}/man3/*
