from src.constants.base_post import BASE_POST

def create_post_content(textos):
    post_content = BASE_POST \
        .replace("Fique Atento ao Prazo do IRPF 2025", textos["subtitulo_1"]) \
        .replace("IRPF 2025: Período de Entrega Previsto para 17 de Março a 30 de Maio", textos["titulo_1"]) \
        .replace("A Receita Federal anunciou que o período para a entrega da Declaração do Imposto de Renda Pessoa Física(IRPF) de 2025 terá início em 17 de março e se estenderá até 30 de maio.", textos["paragrafo_1"]) \
        .replace("Por que é Importante Conhecer o Prazo de Entrega?", textos["subtitulo_2"]) \
        .replace("Evite Multas e Complicações", textos["titulo_2"]) \
        .replace("Cumprir o prazo de entrega da declaração do IRPF é essencial para evitar multas e outras complicações com o Fisco. A entrega dentro do período estipulado garante que o contribuinte esteja em conformidade com a legislação tributária vigente.", textos["paragrafo_2_1"]) \
        .replace("Além disso, quem entrega a declaração nos primeiros dias do prazo tem maiores chances de receber a restituição mais cedo, caso tenha direito a ela. Portanto, estar atento às datas e preparar a documentação com antecedência são medidas fundamentais para um processo tranquilo.", textos["paragrafo_2_2"]) \
        .replace("Passo a Passo para a Declaração do IRPF 2025", textos["subtitulo_3"]) \
        .replace("Passo 1: Reúna Toda a Documentação Necessária", textos["titulo_3_1"]) \
        .replace("Antes de iniciar o preenchimento da declaração, é fundamental reunir todos os documentos necessários, como informes de rendimentos, comprovantes de despesas dedutíveis (saúde, educação, etc.), recibos de pagamentos e outros documentos relevantes.", textos["paragrafo_3_1"]) \
        .replace("Passo 2: Utilize o Programa da Receita Federal", textos["titulo_3_2"]) \
        .replace("Baixe e instale o programa oficial da Receita Federal para a declaração do IRPF 2025. Certifique-se de estar utilizando a versão mais recente para evitar problemas no envio.", textos["paragrafo_3_2"]) \
        .replace("Passo 3: Preencha e Envie a Declaração", textos["titulo_3_3"]) \
        .replace("Com todos os documentos em mãos, preencha a declaração com atenção, revisando todas as informações antes de enviar. Após o envio, guarde o comprovante de entrega e acompanhe o processamento da sua declaração pelo site da Receita Federal.", textos["paragrafo_3_3"]) \
        .replace("Principais Novidades do IRPF 2025", textos["titulo_4"]) \
        .replace("Atualização da Tabela Progressiva", textos["titulo_4_1"]) \
        .replace("Para o ano de 2025, espera-se uma atualização na tabela progressiva do Imposto de Renda, ajustando as faixas de renda e as alíquotas correspondentes. Essa mudança visa corrigir a defasagem acumulada nos últimos anos e tornar o imposto mais justo para os contribuintes.", textos["paragrafo_4_1"]) \
        .replace("Inclusão de Novas Fichas de Declaração", textos["titulo_4_2"]) \
        .replace("De acordo com a Lei 14.754, de 12 de dezembro de 2023, haverá a inclusão de novas fichas na declaração, relacionadas a ganhos em operações financeiras e lucros e dividendos no exterior.", textos["paragrafo_4_2"]) \
        .replace("Ampliação das Deduções Permitidas", textos["titulo_4_3"]) \
        .replace("Espera-se que, para 2025, haja uma ampliação nas possibilidades de deduções, incluindo novos tipos de despesas que poderão ser abatidas da base de cálculo do imposto. Essa medida tem como objetivo incentivar determinados gastos, como investimentos em educação e saúde.", textos["paragrafo_4_3"]) \
        .replace("Dicas para uma Declaração Sem Erros", textos["subtitulo_5"]) \
        .replace("Como Preencher sua Declaração de Forma Correta e Evitar Problemas", textos["titulo_5"]) \
        .replace("Para evitar erros na declaração do IRPF 2025, é recomendável utilizar a declaração pré-preenchida disponibilizada pela Receita Federal, que já contém diversas informações fornecidas por fontes pagadoras e instituições financeiras. Além disso, mantenha todos os comprovantes organizados e, em caso de dúvida, consulte um profissional de contabilidade.", textos["paragrafo_5"]) 
    
    return post_content