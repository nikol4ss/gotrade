<script setup lang="ts">
import Quotation from '@/components/charts/Quotation.vue';
import AreaChart from '@/components/charts/AreaChart.vue';
import DonutChart from '@/components/charts/DonutChart.vue';
import LineChart from '@/components/charts/LineChart.vue';
import BarChart from '@/components/charts/BarChart.vue';

const revenueData = [
    { name: "Jan", total: 1000, predicted: 1200 },
    { name: "Feb", total: 900, predicted: 300 },
];

const portfolioData = [
    { name: "BTC", value: 40 },
    { name: "ETH", value: 25 },
    { name: "ADA", value: 20 },
    { name: "SOL", value: 15 },
];

const lineData = [
    { year: 1970, "Export Growth Rate": 2.04, "Import Growth Rate": 1.53 },
    { year: 1971, "Export Growth Rate": 1.96, "Import Growth Rate": 1.58 },
];

const yFormatter = (tick: number | Date) => {
    if (typeof tick === "number") return `$ ${new Intl.NumberFormat("us").format(tick)}`;
    return "$ 0";
};

const valueFormatter = (tick: number | Date) => {
    if (typeof tick === "number") return `$ ${new Intl.NumberFormat("us").format(tick)}`;
    return "$ 0";
};
</script>


<template>
    <div class="flex flex-1 flex-col gap-6 p-4">

        <div class="grid gap-4 md:grid-cols-2">
            <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
                <h2 class="text-lg font-semibold mb-2">Saldo Total</h2>
                <span class="text-2xl font-bold">$123,456</span>
                <span class="text-sm text-muted-foreground mt-1">Total de todos os investimentos</span>
            </div>
            <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
                <h2 class="text-lg font-semibold mb-2">Gastos</h2>
                <span class="text-2xl font-bold">$5,432</span>
                <span class="text-sm text-muted-foreground mt-1">Gastos nos últimos 30 dias</span>
            </div>
        </div>

        <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
            <h2 class="text-lg font-semibold mb-2">Distribuição por Ativos</h2>
            <DonutChart :data="portfolioData" category="value" :value-formatter="valueFormatter"
                :colors="['blue', 'green', 'orange', 'purple']" />
        </div>

        <div class="grid gap-4 md:grid-cols-2">
            <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
                <h2 class="text-lg font-semibold mb-2">Performance de Carteira</h2>
                <AreaChart :data="revenueData" :categories="['total', 'predicted']" :colors="['blue', 'green']"
                    class="flex-1 w-full h-full" />
            </div>
            <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
                <h2 class="text-lg font-semibold mb-2">Retorno Mensal / ROI</h2>
                <span class="text-muted-foreground">Ganho líquido por tipo de investimento</span>
                <BarChart :data="revenueData" :categories="['total', 'predicted']" :y-formatter="yFormatter"
                    :colors="['blue', 'green']" />
            </div>
        </div>

        <div class="grid gap-4 md:grid-cols-2">
            <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
                <h2 class="text-lg font-semibold mb-2">Cotações e Avaliação</h2>
   
            </div>
            <div class="rounded-xl bg-muted/50 p-4 flex flex-col items-center justify-center h-full">
                <h2 class="text-lg font-semibold mb-2">Indicadores de Risco</h2>
                <span class="text-muted-foreground">Volatilidade, correlação, liquidez...</span>
            </div>
        </div>

        <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-full">
            <h2 class="text-lg font-semibold mb-2">Tendência de Investimentos</h2>
            <LineChart :data="lineData" :categories="['Export Growth Rate', 'Import Growth Rate']"
                :y-formatter="yFormatter" :colors="['blue', 'green']" />
        </div>

        <div class="rounded-xl bg-muted/50 p-4 flex flex-col h-64">
            <h2 class="text-lg font-semibold mb-2">Feedback e Recomendações</h2>
            <div class="flex-1 rounded-xl bg-muted/30 flex items-center justify-center">
                <span class="text-muted-foreground">Sugestões de ajustes e alertas futuros</span>
            </div>
        </div>

    </div>
</template>
