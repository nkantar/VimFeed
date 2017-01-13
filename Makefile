.DEFAULT_GOAL := help

help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

buildsite: ## build site
	mkdir -p ./build/assets ./build/about ./build/list
	./venv/bin/python vimfeed.py
	sass --sourcemap=none assets/style/style.scss:assets/style/style.css
	rm -r build/assets
	cp -r assets build/.
	find ./build -name ".DS_Store" -type f -delete
	find ./build -name ".swp" -type f -delete

redeploy: ## redeploy site to https://vimfeed.github.io
	make buildsite
	git checkout master && git add . && git commit -m "Republishing" && git push origin master

autoredeploy: ## autoredeploy site to https://vimfeed.github.io
	git pull origin master --rebase
	make redeploy
