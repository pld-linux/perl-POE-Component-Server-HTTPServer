#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	POE
%define	pnam	Component-Server-HTTPServer
Summary:	POE::Component::Server::HTTPServer - serve HTTP requests
Summary(pl.UTF-8):	POE::Component::Server::HTTPServer - obsługa żądań HTTP
Name:		perl-POE-Component-Server-HTTPServer
Version:	0.9.2
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	766c06301099868fca4bbc8bd5cb358d
URL:		http://search.cpan.org/dist/POE-Component-Server-HTTPServer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTTP::Message) >= 1.3
BuildRequires:	perl(HTTP::Status)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl-MIME-Types >= 1.06
BuildRequires:	perl-POE
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Server::HTTPServer is a POE-based HTTP server.
Requests are dispatched based on an ordered list of prefix => handler
pairs.

%description -l pl.UTF-8
POE::Component::Server::HTTPServer to serwer HTTP oparty na POE.
Żądania są przekazywane w oparciu o uporządkowaną listę par prefix =>
handler.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/POE/Component/Server/*.pm
%{perl_vendorlib}/POE/Component/Server/HTTPServer
%{_mandir}/man3/*
