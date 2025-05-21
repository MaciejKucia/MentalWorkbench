export default async function(eleventyConfig) {
	eleventyConfig.addPassthroughCopy("style.css");
	eleventyConfig.addPassthroughCopy("logo.png");
	eleventyConfig.addPassthroughCopy("lib/**/*.jpg");
	eleventyConfig.addPassthroughCopy("lib/**/*.png");
	eleventyConfig.addPassthroughCopy("projects/**/*.jpg");
	eleventyConfig.addPassthroughCopy("projects/**/*.png");
	eleventyConfig.addPassthroughCopy("media/**/*");
};
