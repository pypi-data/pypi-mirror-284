from info.basic.decorators import FuncTools
from info.basic.typehint import T, Null, BernBinTP, CatMultTP, BetaTP, DirTP, DirMultTP
from info.basic.core import GenericDiscrete
from info.basic.functions import assert_info_raiser
from typing import Callable, TypeVar, Optional, Union
from scipy import stats as st
Dis = object
PriDis = TypeVar('PriDis')
PosDis = TypeVar('PosDis')
LikeDis = TypeVar('LikeDis')
PreDis = TypeVar('PreDis')


class _Bayes:

    @FuncTools.params_setting(name=T[Null: str], kernel=T[Null: Dis], prior=T[Null: Dis],
                              invalid_check=T[None: Optional[Callable]],
                              update_conjugate=T[Null: Callable[[PriDis, LikeDis], PosDis]],
                              update_predictive=T[Null: Callable[[PosDis, LikeDis], PreDis]])
    def __init__(self, **params):
        self.name = params.get('name')
        self.kernel = params.get('kernel')
        self.conjugate = params.get('prior')
        self.predictive, self._err_pos = None, ValueError('use a mismatch posterior from kernel')
        self.update_conjugate = params.get('update_conjugate')
        self.update_predictive = params.get('update_predictive')
        self.update_posterior()

    @FuncTools.params_setting(posterior=T[None: Optional[Dis]])
    def update_posterior(self, **params):
        posterior = params.get('posterior')
        if posterior is None:
            self._update_posterior()
            self._update_predictive()
        else:
            assert_info_raiser(self._in_homology(posterior), self._err_pos)
            self.conjugate = self.update_conjugate(self.conjugate, posterior)
            self.predictive = self.update_predictive(self.conjugate, posterior)

    @FuncTools.params_setting(posterior=T[Null: Dis])
    def compare_posterior(self, **params):
        posterior = params.get('posterior')
        assert_info_raiser(self._in_homology(posterior), self._err_pos)
        return self.update_conjugate(self.conjugate, posterior)

    def _update_posterior(self):
        self.conjugate = self.update_conjugate(self.conjugate, self.kernel)

    def _update_predictive(self):
        self.predictive = self.update_predictive(self.conjugate, self.kernel)

    def _in_homology(self, x: Dis):
        return type(self.kernel) is type(x)


def _multinomial_conjugate(pri: DirTP, like: CatMultTP) -> DirTP:  # dirichlet * multinomial -> dirichlet
    return st.dirichlet(like.p * like.n + pri.alpha)


def _multinomial_predictive(pos: DirTP, like: CatMultTP) -> DirMultTP:
    return st.dirichlet_multinomial(like.p * like.n + pos.alpha, like.n)


def _discrete_pre_check(p: DirTP, k: GenericDiscrete) -> bool:
    if hasattr(k, 'name') and k.name in ['bernoulli', 'binomial']:
        res = p.alpha.__len__() == 2
    else:
        res = k.p.__len__() == p.alpha.__len__()
    return res


def _init_prior(k: GenericDiscrete, p: Union[DirTP, BetaTP] = None) -> DirTP:
    res = st.dirichlet([1 for _ in range(k.p)]) if p is None else p
    return [x := res.args[0:2], st.dirichlet([_/sum(x) for _ in x])][-1] if (hasattr(res, 'dist') and
                                                                             res.dist.name == 'beta') else res


_observe_to_multi = (lambda x: GenericDiscrete(x) if not isinstance(x, GenericDiscrete) else x)  # generic discrete


def _discrete_base(**params):
    kernel = _observe_to_multi(params.get('kernel'))
    prior = _init_prior(kernel, params.get('prior'))
    assert_info_raiser(kernel.name == params.get('~specific_distribution') and _discrete_pre_check(prior, kernel),
                       ValueError('mismatch of kernel and prior'))
    return _Bayes(name=kernel.name, kernel=kernel, prior=prior, update_conjugate=_multinomial_conjugate,
                  update_predictive=_multinomial_predictive)


@FuncTools.params_setting(kernel=T[Null: BernBinTP], prior=T[None: Optional[Union[BetaTP, DirTP]]],
                          **{'~unknown_tp': [BernBinTP, BetaTP, DirTP]})
def bernoulli(**params):
    return _discrete_base(**{**params, **{'~specific_distribution': 'bernoulli'}})


@FuncTools.params_setting(kernel=T[Null: CatMultTP], prior=T[None: Optional[DirTP]],
                          **{'~unknown_tp': [CatMultTP, DirTP]})
def categorical(**params):  # no scipy api for categorical, init prior use scipy.stats.multinomial(1, p) instead
    return _discrete_base(**{**params, **{'~specific_distribution': 'categorical'}})


@FuncTools.params_setting(kernel=T[Null: BernBinTP], prior=T[None: Optional[Union[BetaTP, DirTP]]],
                          **{'~unknown_tp': [BernBinTP, BetaTP, DirTP]})
def binomial(**params):
    return _discrete_base(**{**params, **{'~specific_distribution': 'binomial'}})


@FuncTools.params_setting(kernel=T[Null: CatMultTP], prior=T[None: Optional[DirTP]],
                          **{'~unknown_tp': [CatMultTP, DirTP]})
def multinomial(**params):
    return _discrete_base(**{**params, **{'~specific_distribution': 'multinomial'}})


if __name__ == '__main__':
    # a = multinomial(kernel=st.multinomial(12, [0.1, 0.3, 0.6]), prior=st.dirichlet([4, 5, 3]))
    # # a = multinomial(kernel=st.multinomial(12, [0.1, 0.3, 0.6]),)
    # print(a.kernel, a.conjugate.alpha, a.predictive.alpha)
    # a._update_posterior()
    # print(a.kernel, a.conjugate.alpha, a.predictive.alpha)
    #
    # a = binomial(kernel=st.binom(12, 0.3), prior=st.beta(4, 5, 8, 1, ))
    # # a = multinomial(kernel=st.multinomial(12, [0.1, 0.3, 0.6]),)
    # print(a.kernel, a.conjugate.alpha, a.predictive.alpha)
    pass
