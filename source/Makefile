SPHINXOPTS    = -D wavedrom_html_jsinline=0
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = ../build

PYTHON=python3

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) ./

.PHONY: clean html linkcheck livepreview generate_markup

clean:
	-rm -rf $(BUILDDIR)/*

generate_markup:
	$(PYTHON) generate_markup.py

html: generate_markup
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck

livepreview:
	bash -c '$(MAKE) html ; $(PYTHON) -B -c "import livepreviewhtml; livepreviewhtml.previewHtml()"'
