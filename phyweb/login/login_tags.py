from django.utils.safestring import mark_safe
import markdown

@register.filter(name="markdown")
	def markdown format(text):
		return mark_safe(markdown.markdown(text))