<script setup lang="ts">
import Quotation from '@/components/charts/Quotation.vue'
import AreaChart from '@/components/charts/AreaChart.vue'
import DonutChart from '@/components/charts/DonutChart.vue'
import LineChart from '@/components/charts/LineChart.vue'
import BarChart from '@/components/charts/BarChart.vue'

const revenueData = [
    { name: 'Jan', total: 1000, predicted: 1200 },
    { name: 'Feb', total: 900, predicted: 300 },
]

const portfolioData = [
    { name: 'BTC', value: 40 },
    { name: 'ETH', value: 25 },
    { name: 'PETR4', value: 20 },
    { name: 'IVVB11', value: 15 },
]

const lineData = [
    { year: 1970, 'Export Growth Rate': 2.04, 'Import Growth Rate': 1.53 },
    { year: 1971, 'Export Growth Rate': 1.96, 'Import Growth Rate': 1.58 },
]

const yFormatter = (tick: number | Date) =>
    typeof tick === 'number' ? `$ ${new Intl.NumberFormat('us').format(tick)}` : '$ 0'

const valueFormatter = (tick: number | Date) =>
    typeof tick === 'number' ? `$ ${new Intl.NumberFormat('us').format(tick)}` : '$ 0'

const quotationData = [
    { asset: "BTC", price: 123456, variation: "+2.3%" },
    { asset: "PETR4", price: 32.45, variation: "-0.8%" },
    { asset: "IVVB11", price: 285.10, variation: "+1.1%" },
]
</script>

<template>
    <div class="flex flex-1 flex-col gap-6 p-6 min-w-0">
        <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
            <div class="rounded-2xl bg-muted/50 p-4 flex flex-col">
                <h2 class="text-base font-medium">Saldo Total</h2>
                <span class="text-2xl font-bold mt-1">$123,456</span>
                <span class="text-xs text-muted-foreground">Total de todos os investimentos</span>
            </div>
            <div class="rounded-2xl bg-muted/50 p-4 flex flex-col">
                <h2 class="text-base font-medium">Gastos</h2>
                <span class="text-2xl font-bold mt-1">$5,432</span>
                <span class="text-xs text-muted-foreground">Últimos 30 dias</span>
            </div>
            <div class="rounded-2xl bg-muted/50 p-4 flex flex-col">
                <h2 class="text-base font-medium">Rentabilidade</h2>
                <span class="text-2xl font-bold mt-1">+12.5%</span>
                <span class="text-xs text-muted-foreground">Ano atual (YTD)</span>
            </div>
            <div class="rounded-2xl bg-muted/50 p-4 flex flex-col">
                <h2 class="text-base font-medium">Risco Médio</h2>
                <span class="text-2xl font-bold mt-1">Baixo</span>
                <span class="text-xs text-muted-foreground">Perfil de risco da carteira</span>
            </div>
        </div>

        <div class="rounded-2xl bg-muted/50 p-6">
            <h2 class="text-lg font-semibold mb-4">Performance da Carteira</h2>
            <AreaChart :data="revenueData" :categories="['total', 'predicted']" :colors="['blue', 'green']"
                class="w-full h-64" />

        </div>

        <div class="grid gap-6 md:grid-cols-2">
            <div class="rounded-2xl bg-muted/50 p-6">
                <h2 class="text-lg font-semibold mb-4">Distribuição por Ativos</h2>
                <DonutChart :data="portfolioData" category="value" :value-formatter="valueFormatter"
                    :colors="['blue', 'green', 'orange', 'purple']" />
            </div>
            <div class="rounded-2xl bg-muted/50 p-6">
                <h2 class="text-lg font-semibold mb-2">Retorno Mensal / ROI</h2>
                <span class="text-sm text-muted-foreground">Ganho líquido por tipo de investimento</span>
                <BarChart :data="revenueData" :categories="['total', 'predicted']" :y-formatter="yFormatter"
                    :colors="['blue', 'green']" class="mt-4" />
            </div>
        </div>

        <div class="grid gap-6 md:grid-cols-2">
            <div class="rounded-2xl bg-muted/50 p-6">
                <h2 class="text-lg font-semibold mb-4">Cotações e Avaliação</h2>
                <Quotation :data="quotationData" :columns="[
                    { key: 'asset', label: 'Ativo' },
                    { key: 'price', label: 'Preço' },
                    { key: 'variation', label: 'Variação' }
                ]" />

            </div>
            <div class="rounded-2xl bg-muted/50 p-6">
                <h2 class="text-lg font-semibold mb-2">Indicadores de Risco</h2>
                <span class="text-sm text-muted-foreground">Volatilidade, correlação, liquidez...</span>
                <div class="mt-4 flex flex-col gap-2">
                    <div class="flex justify-between text-sm">
                        <span>Volatilidade</span><span class="font-semibold">Média</span>
                    </div>
                    <div class="flex justify-between text-sm">
                        <span>Liquidez</span><span class="font-semibold">Alta</span>
                    </div>
                    <div class="flex justify-between text-sm">
                        <span>Correlação</span><span class="font-semibold">Baixa</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="rounded-2xl bg-muted/50 p-6">
            <h2 class="text-lg font-semibold mb-4">Tendência de Investimentos</h2>
            <LineChart :data="lineData" :categories="['Export Growth Rate', 'Import Growth Rate']"
                :y-formatter="yFormatter" :colors="['blue', 'green']" class="h-72" />
        </div>

        <div class="rounded-2xl bg-muted/50 p-6 flex flex-col h-64">
            <h2 class="text-lg font-semibold mb-2">Feedback e Recomendações</h2>
            <div class="flex-1 rounded-xl bg-muted/30 flex items-center justify-center">
                <span class="text-muted-foreground">Sugestões de ajustes e alertas futuros</span>
            </div>
        </div>

    </div>
</template>
