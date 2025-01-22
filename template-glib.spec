%global api 1.0
%global major 0
%define libname %mklibname template_glib %{api} %{major}
%define girname %mklibname template-gir %{api}
%define devname %mklibname -d template_glib %{api}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		template-glib
Version:	3.36.3
Release:	1
Summary:	A templating library for GLib
Group:		Graphical desktop/GNOME

License:	LGPLv2+
URL:		https://git.gnome.org/browse/template-glib/
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	gtk-doc
BuildRequires:	meson
BuildRequires:	vala
BuildRequires:	vala-tools

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)


%description
Template-GLib is a templating library for GLib. It includes a simple template
format along with integration into GObject-Introspection for properties and
methods. It separates the parsing of templates and the expansion of templates
for faster expansion. You can also define scope, custom functions, and more
with the embedded expression language.

%package	i18n
Summary:	Internationalization and locale data for %{name}
Group:		System/Internationalization
BuildArch:	noarch
Conflicts:	lib64template_glib0 < 3.28.0-2
Conflicts:	libtemplate_glib0 < 3.28.0-2

%description	i18n
Internationalization and locale data for %{name}.

%package        -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}-%{release}
Obsoletes:	%{_lib}template_glib0 < 3.28.0-2

%description    -n %{libname}
Template-GLib is a templating library for GLib. It includes a simple template
format along with integration into GObject-Introspection for properties and
methods. It separates the parsing of templates and the expansion of templates
for faster expansion. You can also define scope, custom functions, and more
with the embedded expression language.

%package	-n %{girname}
Summary:	GObject introspection interface library for Template
Group:		System/Libraries
Conflicts:	%{_lib}template_glib0 < 3.28.0-2

%description	-n %{girname}
GObject introspection interface library for Template.

%package        -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}template_glib-devel < 3.28.0-2

%description    -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang template-glib

%files i18n -f template-glib.lang

%files -n %{libname}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libtemplate_glib-%{api}.so.%{major}{,.*}

%files -n %{girname}
%{_libdir}/girepository-1.0/Template-%{api}.typelib

%files -n %{devname}
%{_datadir}/gir-1.0/Template-%{api}.gir
%{_datadir}/vala/vapi/template-glib-%{api}.*
%{_includedir}/*
%{_libdir}/libtemplate_glib-%{api}.so
%{_libdir}/pkgconfig/template-glib-%{api}.pc
