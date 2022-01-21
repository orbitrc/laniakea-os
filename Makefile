default:
	./buildiso -f -p desktop

query:
	./buildiso -q -v -p desktop

package:
	mkdir -p pkgbuild
	./packages.py

clean:
	rm -rf pkgbuild
	rm -rf laniakea-repo
