SHELL=/bin/bash -e

FINAL_DIR:=$(CURDIR)/bin
TEMP_DIR:=$(CURDIR)/tmp

# Following are the configuration details for FQZCOMP
FQZ_URL:="http://downloads.sourceforge.net/project/fqzcomp/fqzcomp-4.6.tar.gz"
FQZ_FILE:="fqzcomp-4.6.tar.gz"
FQZ_VS:="4.6"
FQZ_SHA=fa5554747f1d49d1ae2303d6302822416bc318b3

SCALCE_NAME:="scalce"

QUIP_NAME="quip"

all: fqzcomp scalcecomp quipcomp

fqzcomp:
	mkdir -p $(FINAL_DIR)
	mkdir -p $(TEMP_DIR)
	echo "Building FQZCOMP fastQ compression tool."
	curl -L $(FQZ_URL) > $(TEMP_DIR)/$(FQZ_FILE)
	[[  $$(shasum $(TEMP_DIR)/$(FQZ_FILE) | cut -f 1 -d ' ') == $(FQZ_SHA) ]]
	tar -xzf $(TEMP_DIR)/$(FQZ_FILE) -C $(TEMP_DIR)
	$(MAKE) -C $(TEMP_DIR)/fqzcomp-$(FQZ_VS)
	cp $(TEMP_DIR)/fqzcomp-$(FQZ_VS)/fqz_comp $(FINAL_DIR)
	rm -rf $(TEMP_DIR)/fqzcomp-$(FQZ_VS)
	rm $(TEMP_DIR)/$(FQZ_FILE)

scalcecomp:
	echo "Building SCALCECOMP fastQ compression tool."

	git clone https://github.com/sfu-compbio/scalce.git $(TEMP_DIR)/$(SCALCE_NAME)
	$(MAKE) -C $(TEMP_DIR)/$(SCALCE_NAME)
	cp $(TEMP_DIR)/$(SCALCE_NAME)/$(SCALCE_NAME) $(FINAL_DIR)
	rm -rf $(TEMP_DIR)/$(SCALCE_NAME)

quipcomp:
	echo "Building Quip fastQ compression tool."

	git clone git://github.com/dcjones/quip.git $(TEMP_DIR)/$(QUIP_NAME)
	cd $(TEMP_DIR)/$(QUIP_NAME); autoreconf -i && ./configure --prefix=$(TEMP_DIR) && $(MAKE) install; \
	cp $(TEMP_DIR)/bin/quip $(FINAL_DIR)
	cp $(TEMP_DIR)/bin/fastqmd5 $(FINAL_DIR)
	cp $(TEMP_DIR)/bin/bammd5 $(FINAL_DIR)
	rm -rf $(TEMP_DIR)/$(QUIP_NAME)
	rm -rf $(TEMP_DIR)/*

