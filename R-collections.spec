#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-collections
Version  : 0.3.5
Release  : 27
URL      : https://cran.r-project.org/src/contrib/collections_0.3.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/collections_0.3.5.tar.gz
Summary  : High Performance Container Data Types
Group    : Development/Tools
License  : MIT
Requires: R-collections-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
as queues, stacks, deques, dicts and ordered dicts. Benchmarks

%package lib
Summary: lib components for the R-collections package.
Group: Libraries

%description lib
lib components for the R-collections package.


%prep
%setup -q -c -n collections
cd %{_builddir}/collections

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640990976

%install
export SOURCE_DATE_EPOCH=1640990976
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library collections
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library collections
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library collections
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc collections || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/collections/DESCRIPTION
/usr/lib64/R/library/collections/INDEX
/usr/lib64/R/library/collections/LICENSE
/usr/lib64/R/library/collections/Meta/Rd.rds
/usr/lib64/R/library/collections/Meta/features.rds
/usr/lib64/R/library/collections/Meta/hsearch.rds
/usr/lib64/R/library/collections/Meta/links.rds
/usr/lib64/R/library/collections/Meta/nsInfo.rds
/usr/lib64/R/library/collections/Meta/package.rds
/usr/lib64/R/library/collections/NAMESPACE
/usr/lib64/R/library/collections/R/collections
/usr/lib64/R/library/collections/R/collections.rdb
/usr/lib64/R/library/collections/R/collections.rdx
/usr/lib64/R/library/collections/help/AnIndex
/usr/lib64/R/library/collections/help/aliases.rds
/usr/lib64/R/library/collections/help/collections.rdb
/usr/lib64/R/library/collections/help/collections.rdx
/usr/lib64/R/library/collections/help/paths.rds
/usr/lib64/R/library/collections/html/00Index.html
/usr/lib64/R/library/collections/html/R.css
/usr/lib64/R/library/collections/tests/testthat.R
/usr/lib64/R/library/collections/tests/testthat/test-cls.R
/usr/lib64/R/library/collections/tests/testthat/test-deque.R
/usr/lib64/R/library/collections/tests/testthat/test-dict.R
/usr/lib64/R/library/collections/tests/testthat/test-ordered_dict.R
/usr/lib64/R/library/collections/tests/testthat/test-priority_queue.R
/usr/lib64/R/library/collections/tests/testthat/test-queue.R
/usr/lib64/R/library/collections/tests/testthat/test-stack.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/collections/libs/collections.so
/usr/lib64/R/library/collections/libs/collections.so.avx2
/usr/lib64/R/library/collections/libs/collections.so.avx512
