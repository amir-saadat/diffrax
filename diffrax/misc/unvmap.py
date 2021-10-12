import jax
import jax.interpreters.batching as batching
import jax.interpreters.xla as xla
import jax.numpy as jnp


unvmap_all_p = jax.core.Primitive("unvmap_all")


def unvmap_all(x):
    return unvmap_all_p.bind(x)


def _unvmap_all_impl(x):
    return jnp.all(x)


def _unvmap_all_abstract_eval(x):
    return jax.ShapedArray(shape=(), dtype=jax.numpy.bool_.dtype)


def _unvmap_all_batch(x, batch_axes):
    (x,) = x
    return unvmap_all(x), batching.not_mapped


unvmap_all_p.def_impl(_unvmap_all_impl)
unvmap_all_p.def_abstract_eval(_unvmap_all_abstract_eval)
batching.primitive_batchers[unvmap_all_p] = _unvmap_all_batch
xla.translations_with_avals[unvmap_all_p] = xla.lower_fun(
    _unvmap_all_impl, multiple_results=False, with_avals=True
)


unvmap_any_p = jax.core.Primitive("unvmap_any")


def unvmap_any(x):
    return unvmap_any_p.bind(x)


def _unvmap_any_impl(x):
    return jnp.any(x)


def _unvmap_any_abstract_eval(x):
    return jax.ShapedArray(shape=(), dtype=jax.numpy.bool_.dtype)


def _unvmap_any_batch(x, batch_axes):
    (x,) = x
    return unvmap_any(x), batching.not_mapped


unvmap_any_p.def_impl(_unvmap_any_impl)
unvmap_any_p.def_abstract_eval(_unvmap_any_abstract_eval)
batching.primitive_batchers[unvmap_any_p] = _unvmap_any_batch
xla.translations_with_avals[unvmap_any_p] = xla.lower_fun(
    _unvmap_any_impl, multiple_results=False, with_avals=True
)
