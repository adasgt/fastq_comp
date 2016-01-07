SHELL=/bin/bash -e

FINAL_DIR:=$(DEST)/fastq_comp/static
TEMP_DIR:=$(TMP)
FQZ_URL:="http://downloads.sourceforge.net/project/fqzcomp/fqzcomp-4.6.tar.gz"
FQZ_FILE:="fqzcomp-4.6.tar.gz"
FQZ_VS:="4.6"

fqzcomp:
	mkdir -p $(FINAL_DIR)
	mkdir -p $(TEMP_DIR)
	curl -L $(FQZ_URL) > $(TEMP_DIR)/$(FQZ_FILE)
	tar -xzf $(TEMP_DIR)/$(FQZ_FILE) -C $(TEMP_DIR)
	$(MAKE) -C $(TEMP_DIR)/fqzcomp-$(FQZ_VS)
	cp $(TEMP_DIR)/fqzcomp-$(FQZ_VS)/fqz_comp $(FINAL_DIR)
	rm -rf $(TEMP_DIR)

all: fqzcomp