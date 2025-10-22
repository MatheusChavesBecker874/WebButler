from django.test import TestCase
import pytest
from django.core.exceptions import ValidationError
from datetime import time
from .models import Rotina, Aula

@pytest.mark.django_db
def test_c1_cadastrar_rotina_valida():
    r = Rotina.objects.create(nome="Rotina 2025.2")
    assert r.nome == "Rotina 2025.2"

@pytest.mark.django_db
def test_c2_impedir_sobreposicao():
    rotina = Rotina.objects.create(nome="Rotina Teste")
    Aula.objects.create(rotina=rotina, disciplina="Cálculo", dia="seg",
                        inicio=time(8,0), fim=time(10,0))

    a2 = Aula(rotina=rotina, disciplina="Física", dia="seg",
              inicio=time(9,30), fim=time(11,0))

    with pytest.raises(ValidationError) as e:
        a2.full_clean()
    assert "Conflito" in str(e.value)

@pytest.mark.django_db
def test_c3_validacao_campos_obrigatorios():
    r = Rotina(nome="")
    with pytest.raises(ValidationError) as e:
        r.full_clean()
    assert "Nome da rotina é obrigatório" in str(e.value)