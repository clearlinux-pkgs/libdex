#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v19
# autospec commit: f35655a
#
Name     : libdex
Version  : 0.8.0
Release  : 10
URL      : https://gitlab.gnome.org/GNOME/libdex/-/archive/0.8.0/libdex-0.8.0.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/libdex/-/archive/0.8.0/libdex-0.8.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libdex-data = %{version}-%{release}
Requires: libdex-lib = %{version}-%{release}
Requires: libdex-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(liburing)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Dex
Dex provides Future-based programming for GLib-based applications.
It both integrates with and brings new features for application and library
authors who want to structure concurrent code in an easy to manage way.

%package data
Summary: data components for the libdex package.
Group: Data

%description data
data components for the libdex package.


%package dev
Summary: dev components for the libdex package.
Group: Development
Requires: libdex-lib = %{version}-%{release}
Requires: libdex-data = %{version}-%{release}
Provides: libdex-devel = %{version}-%{release}
Requires: libdex = %{version}-%{release}

%description dev
dev components for the libdex package.


%package lib
Summary: lib components for the libdex package.
Group: Libraries
Requires: libdex-data = %{version}-%{release}
Requires: libdex-license = %{version}-%{release}

%description lib
lib components for the libdex package.


%package license
Summary: license components for the libdex package.
Group: Default

%description license
license components for the libdex package.


%prep
%setup -q -n libdex-0.8.0
cd %{_builddir}/libdex-0.8.0
pushd ..
cp -a libdex-0.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726527362
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs
cd ../buildavx2;
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libdex
cp %{_builddir}/libdex-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libdex/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Dex-1.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libdex-1.deps
/usr/share/vala/vapi/libdex-1.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libdex-1/dex-aio.h
/usr/include/libdex-1/dex-async-pair.h
/usr/include/libdex-1/dex-async-result.h
/usr/include/libdex-1/dex-block.h
/usr/include/libdex-1/dex-cancellable.h
/usr/include/libdex-1/dex-channel.h
/usr/include/libdex-1/dex-delayed.h
/usr/include/libdex-1/dex-enums.h
/usr/include/libdex-1/dex-error.h
/usr/include/libdex-1/dex-fiber.h
/usr/include/libdex-1/dex-future-set.h
/usr/include/libdex-1/dex-future.h
/usr/include/libdex-1/dex-gio.h
/usr/include/libdex-1/dex-init.h
/usr/include/libdex-1/dex-main-scheduler.h
/usr/include/libdex-1/dex-object.h
/usr/include/libdex-1/dex-platform.h
/usr/include/libdex-1/dex-promise.h
/usr/include/libdex-1/dex-scheduler.h
/usr/include/libdex-1/dex-static-future.h
/usr/include/libdex-1/dex-thread-pool-scheduler.h
/usr/include/libdex-1/dex-timeout.h
/usr/include/libdex-1/dex-unix-signal.h
/usr/include/libdex-1/dex-version-macros.h
/usr/include/libdex-1/dex-version.h
/usr/include/libdex-1/libdex.h
/usr/lib64/libdex-1.so
/usr/lib64/pkgconfig/libdex-1.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libdex-1.so.1.0.0
/usr/lib64/libdex-1.so.1
/usr/lib64/libdex-1.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libdex/01a6b4bf79aca9b556822601186afab86e8c4fbf
