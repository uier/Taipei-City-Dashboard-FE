<!-- Developed by :thinking: @ 2023 Taipei CodeFest -->

<script setup>
import { defineProps, computed } from "vue";

const props = defineProps([
	"chart_config",
	"activeChart",
	"series",
	"map_config",
]);

const scale = computed(() => {
	if (props.series.data.length > 0) {
		return 1;
	}
	for (let i = 1; i <= 10000; i *= 10) {
		if (props.series.data / i < 100) {
			return i;
		}
	}
	return 10000;
});
const sum = computed(() => {
	return props.series.data.reduce((a, b) => a + b, 0);
});
</script>

<template>
	<div v-if="activeChart === 'PictogramChart'">
		<div class="pictogramchart">
			<div class="pictogramchart-topbar">
				<h5 class="pictogramchart-title" v-if="series.data.length > 0">
					{{ `${series.name}` }}
				</h5>
				<h5 class="pictogramchart-title" v-else>
					{{ `${series.name} ${series.data} ${chart_config.unit}` }}
				</h5>
				<h6 class="pictogramchart-legend" v-if="scale > 1">
					<span style="font-family: var(--font-icon)">{{
						chart_config.icon
					}}</span>
					{{ ` = ${scale} ${chart_config.unit}` }}
				</h6>
				<h6
					class="pictogramchart-catelegend"
					v-if="chart_config.categories"
				>
					<div
						v-for="(cate, index) in chart_config.categories"
						:key="cate"
						:style="{
							display: flex,
							alignItems: center,
							marginRight:
								index === chart_config.categories.length - 1
									? '0'
									: '12px',
						}"
					>
						<span
							:style="{
								fontFamily: 'var(--font-icon)',
								color: chart_config.color[index],
							}"
							>{{ chart_config.icon }}</span
						>
						{{ `${cate}${chart_config.unit}` }}
					</div>
				</h6>
			</div>
			<div class="pictogramchart-content" v-if="series.data.length > 0">
				<template v-for="(val, index) in series.data" :key="val">
					<span
						v-for="i in Math.round((val / sum) * 100)"
						:key="i"
						:style="{
							color: chart_config.color[index],
							fontFamily: 'var(--font-icon)',
						}"
					>
						{{ chart_config.icon }}
					</span>
				</template>
			</div>
			<div class="pictogramchart-content" v-else>
				<span
					v-for="i in series.data"
					:key="i"
					:style="{
						color: chart_config.color,
						fontFamily: 'var(--font-icon)',
					}"
				>
					{{ chart_config.icon }}
				</span>
			</div>
		</div>
	</div>
</template>

<style scoped lang="scss">
.pictogramchart {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	width: 100%;
	height: 100%;
	padding: 10px;

	&-topbar {
		width: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 6px;
		padding-right: 18px;
	}

	&-title {
		font-size: var(--font-m);
		font-weight: 500;
	}

	&-legend {
		font-size: var(--font-s);
		font-weight: 400;
	}

	&-catelegend {
		display: flex;
		align-items: center;
	}

	&-content {
		display: grid;
		width: 100%;
		grid-template-columns: repeat(10, 1fr);
		grid-template-rows: repeat(10, 1fr);
		font-size: var(--font-l);

		> span {
			// Assuming each grid item is a span
			animation: ease-in 0.2s forwards; // Apply the animation, adjust duration as needed
			opacity: 0;
		}

		// Generate staggered animations for each item
		@for $i from 1 through 100 {
			// Adjust the number based on your grid size
			> span:nth-child(#{$i}) {
				animation-delay: $i *
					0.01s; // Stagger the delay, adjust timing as needed
			}
		}
	}
}

@keyframes ease-in {
	0% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
}
</style>
