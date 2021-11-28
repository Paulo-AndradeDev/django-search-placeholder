import re

PLACEHOLDER_PREFIX = "请输入 "

try:
    from django.conf import settings
except ImportError:
    ...
else:
    if (_p := getattr(settings, "PLACEHOLDER_PREFIX", None)) is not None:
        PLACEHOLDER_PREFIX = _p

RE_PREFIX = re.compile(r"[=^]")


class PlaceholderMixin:
    """Auto generate placeholder in search input"""

    change_list_template = "search_placeholder/change_list.html"
    placeholder_prefix = PLACEHOLDER_PREFIX

    def changelist_view(self, request, extra_context=None):
        if fs := getattr(self, "search_fields", None):
            if search_placeholder := getattr(self, "search_placeholder", True):
                extra_context = extra_context or {}
                if search_placeholder is True:
                    meta = self.model._meta
                    names = []
                    for field in fs:
                        field = RE_PREFIX.sub("", field)
                        if "__" not in field:
                            names.append(meta.get_field(field).verbose_name)
                        else:
                            fn, nxt, *_ = field.split("__")
                            f_obj = meta.get_field(fn)
                            n = getattr(f_obj, "verbose_name", "")
                            if remote_field := f_obj.remote_field:
                                r_meta = remote_field.model._meta
                                if (r_n := r_meta.get_field(nxt).verbose_name) != n:
                                    n += r_n
                            if not n:
                                n = f_obj.name
                            names.append(n)
                    search_placeholder = self.placeholder_prefix + "/".join(names)
                extra_context["search_placeholder"] = search_placeholder
        return super().changelist_view(request, extra_context)
