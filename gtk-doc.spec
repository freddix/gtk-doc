%include	/usr/lib/rpm/macros.perl

Summary:	API documentation generation tool for GTK+ and GNOME
Name:		gtk-doc
Version:	1.20
Release:	2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk-doc/1.20/%{name}-%{version}.tar.xz
# Source0-md5:	58532fed036f72fc3bfd4fe79473247b
URL:		http://www.gtk.org/rdp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	itstool
BuildRequires:	libxslt-progs
BuildRequires:	openjade
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	source-highlight
Requires:	docbook-dtd412-xml
Requires:	docbook-style-dsssl
Requires:	docbook-style-xsl
Requires:	libxslt-progs
Requires:	openjade
Requires:	source-highlight
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# architecture-independant pkgconfig dir
%define		_pkgconfigdir	%{_datadir}/pkgconfig

%description
gtk-doc is a tool for generating API reference documentation. It is
used for generating the documentation for GTK+, GLib and GNOME.

%package common
Summary:	Common directories for documetation generated using gtk-doc
Group:		Development

%description common
Common directories for API documentation for various packages,
generated using gtk-doc.

%package examples
Summary:	gtk-doc examples
Group:		Development

%description examples
gtk-doc examples.

%prep
%setup -q
mv -f doc/README doc/README.docs

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/gtk-doc/html

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS TODO README doc/*
%attr(755,root,root) %{_bindir}/gtkdoc-*
%attr(755,root,root) %{_bindir}/gtkdocize
%{_datadir}/gtk-doc
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/%{name}.pc
%{_datadir}/sgml/%{name}

%files common
%defattr(644,root,root,755)
%dir %{_docdir}/gtk-doc
%dir %{_gtkdocdir}

