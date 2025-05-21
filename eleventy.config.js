import eleventyPluginMathjax from "eleventy-plugin-mathjax";

export default async function(eleventyConfig) {
	eleventyConfig.addPlugin(eleventyPluginMathjax);
	eleventyConfig.addPassthroughCopy("style.css");
	eleventyConfig.addPassthroughCopy("logo.png");
	eleventyConfig.addPassthroughCopy("lib/**/*.jpg");
	eleventyConfig.addPassthroughCopy("lib/**/*.png");
	eleventyConfig.addPassthroughCopy("projects/**/*.jpg");
	eleventyConfig.addPassthroughCopy("projects/**/*.png");
	eleventyConfig.addPassthroughCopy("projects/**/*.svg");
	eleventyConfig.addPassthroughCopy("projects/**/*.gif");
	eleventyConfig.addPassthroughCopy("media/**/*");
};
