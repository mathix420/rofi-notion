.PHONY: all clean build deploy aur

AUR_BUILD_DIR = /tmp/aur-build/rofi-notion

all: clean build deploy

aur:
	rm -rf $(AUR_BUILD_DIR)
	git clone ssh://aur@aur.archlinux.org/rofi-notion.git $(AUR_BUILD_DIR)
	makepkg --printsrcinfo > $(AUR_BUILD_DIR)/.SRCINFO
	cp PKGBUILD $(AUR_BUILD_DIR)
	git -C $(AUR_BUILD_DIR) add PKGBUILD .SRCINFO
	git -C $(AUR_BUILD_DIR) commit -m "Add `git describe --tags | cut -d"-" -f1`"
	git -C $(AUR_BUILD_DIR) push

clean:
	rm -rf dist/
	rm -rf $(AUR_BUILD_DIR)

build:
	pip install -U build
	python3 -m build

deploy:
	pip install -U twine
	python3 -m twine upload dist/*
