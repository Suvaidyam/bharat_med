<template>
	<div class="reactions-container">
		<div class="card shadow">
			<!-- Header -->
			<div class="card-header d-flex justify-content-between align-items-center">
				<h5 class="mb-0 text-dark">Reactions</h5>
				<button class="close-btn">
					<svg
						class="icon-md text-muted"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M6 18L18 6M6 6l12 12"
						></path>
					</svg>
				</button>
			</div>

			<!-- Tab Navigation -->
			<div class="border-bottom">
				<div class="d-flex">
					<button
						v-for="tab in tabs"
						:key="tab.key"
						class="tab-button d-flex align-items-center gap-2"
						:class="{ active: activeTab === tab.key }"
						@click="setActiveTab(tab.key)"
					>
						<span v-if="tab.icon" v-html="tab.icon"></span>
						<span>{{ tab.label }}</span>
						<span v-if="tab.count > 0" class="badge bg-secondary badge-count">{{
							tab.count
						}}</span>
					</button>
				</div>
			</div>

			<!-- Reactions List -->
			<div class="reactions-list">
				<div v-if="filteredReactions.length === 0" class="text-center p-5 text-muted">
					<small>No {{ activeTab === 'all' ? '' : activeTab }} reactions yet</small>
				</div>

				<div v-else>
					<div
						v-for="person in filteredReactions"
						:key="person.id"
						class="reaction-item d-flex justify-content-between align-items-center p-3"
					>
						<div class="d-flex align-items-center gap-3">
							<!-- Avatar -->
							<div class="avatar rounded-circle" :class="person.color">
								{{ person.avatar }}
							</div>

							<!-- User Info -->
							<div class="flex-grow-1">
								<h6 class="mb-0 text-dark small">{{ person.name }}</h6>
								<small class="text-muted">{{ person.role }}</small>
							</div>
						</div>

						<!-- Reaction Icon -->
						<div class="ms-2">
							<span v-html="getReactionIcon(person.reaction)"></span>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const activeTab = ref('all')

const reactions = ref([
	{
		id: 1,
		name: 'Ankita Kumari Singh',
		role: 'UI/UX',
		avatar: 'AK',
		reaction: 'like',
		color: 'bg-green-500',
	},
	{
		id: 2,
		name: 'Bhargavi Jain',
		role: 'Associate Product Manager',
		avatar: 'BJ',
		reaction: 'love',
		color: 'bg-red-500',
	},
	{
		id: 3,
		name: 'Namandeep',
		role: 'Data Analyst',
		avatar: 'N',
		reaction: 'like',
		color: 'bg-blue-500',
	},
	{
		id: 4,
		name: 'Anamika',
		role: 'Product Manager',
		avatar: 'A',
		reaction: 'highfive',
		color: 'bg-purple-500',
	},
	{
		id: 5,
		name: 'Divyanshi Agarwal',
		role: 'Product Analyst',
		avatar: 'DA',
		reaction: 'love',
		color: 'bg-orange-500',
	},
	{
		id: 6,
		name: 'Harsh Kumar',
		role: 'SDE-2, Backend',
		avatar: 'HK',
		reaction: 'like',
		color: 'bg-teal-500',
	},
	{
		id: 7,
		name: 'Ankit',
		role: 'SDE-2, Android',
		avatar: 'A',
		reaction: 'highfive',
		color: 'bg-indigo-500',
	},
	{
		id: 8,
		name: 'Shahid Parvez',
		role: 'Data Analyst',
		avatar: 'SP',
		reaction: 'love',
		color: 'bg-pink-500',
	},
])

// Computed properties
const reactionCounts = computed(() => {
	const counts = { love: 0, like: 0, highfive: 0 }
	reactions.value.forEach((reaction) => {
		counts[reaction.reaction]++
	})
	return counts
})

const filteredReactions = computed(() => {
	return activeTab.value === 'all'
		? reactions.value
		: reactions.value.filter((reaction) => reaction.reaction === activeTab.value)
})

const tabs = computed(() => [
	{ key: 'all', label: 'All', count: reactions.value.length },
	{
		key: 'love',
		label: 'Love',
		icon: '<svg class="icon-sm text-red-500" fill="currentColor" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
		count: reactionCounts.value.love,
	},
	{
		key: 'like',
		label: 'Like',
		icon: '<svg class="icon-sm text-blue-500" fill="currentColor" viewBox="0 0 24 24"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>',
		count: reactionCounts.value.like,
	},
	{
		key: 'highfive',
		label: 'High Five',
		icon: '<svg class="icon-sm text-yellow-500" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 11.5V14m0-2.5v-6a1.5 1.5 0 1 1 3 0m-3 6a1.5 1.5 0 0 0-3 0v2a7.5 7.5 0 0 0 15 0v-5a1.5 1.5 0 0 0-3 0m-6-3V11m0-5.5v-1a1.5 1.5 0 0 1 3 0v1m0 0V11m0-5.5a1.5 1.5 0 0 1 3 0v3m0 0V11"/></svg>',
		count: reactionCounts.value.highfive,
	},
])

// Methods
const getReactionIcon = (reaction) => {
	const icons = {
		love: '<svg class="icon-md text-red-500" fill="currentColor" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
		like: '<svg class="icon-md text-blue-500" fill="currentColor" viewBox="0 0 24 24"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>',
		highfive:
			'<svg class="icon-md text-yellow-500" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 11.5V14m0-2.5v-6a1.5 1.5 0 1 1 3 0m-3 6a1.5 1.5 0 0 0-3 0v2a7.5 7.5 0 0 0 15 0v-5a1.5 1.5 0 0 0-3 0m-6-3V11m0-5.5v-1a1.5 1.5 0 0 1 3 0v1m0 0V11m0-5.5a1.5 1.5 0 0 1 3 0v3m0 0V11"/></svg>',
	}
	return icons[reaction] || ''
}

const setActiveTab = (tabKey) => {
	activeTab.value = tabKey
}
</script>

<style scoped>
.reactions-container {
	max-width: 30rem;
	margin: 0 auto;
}

.avatar {
	width: 2.5rem;
	height: 2.5rem;
	display: flex;
	align-items: center;
	justify-content: center;
	color: white;
	font-weight: 600;
	font-size: 0.875rem;
}

.bg-green-500 {
	background-color: #10b981 !important;
}

.bg-red-500 {
	background-color: #ef4444 !important;
}

.bg-blue-500 {
	background-color: #3b82f6 !important;
}

.bg-purple-500 {
	background-color: #8b5cf6 !important;
}

.bg-orange-500 {
	background-color: #f97316 !important;
}

.bg-teal-500 {
	background-color: #14b8a6;
}

.bg-indigo-500 {
	background-color: #6366f1 !important;
}

.bg-pink-500 {
	background-color: #ec4899 !important;
}

.reaction-item:hover {
	background-color: #f8f9fa !important;
}

.tab-button {
	border: none;
	background: none;
	padding: 0.75rem 1rem;
	border-bottom: 2px solid transparent;
	transition: all 0.2s;
}

.tab-button:hover {
	background-color: #f8f9fa;
	color: #495057;
}

.tab-button.active {
	border-bottom-color: #0d6efd !important;
	color: #0d6efd !important;
	background-color: rgba(13, 110, 253, 0.1);
}

.close-btn {
	border: none;
	background: none;
	padding: 0.25rem;
	border-radius: 50%;
	transition: background-color 0.2s;
}

.close-btn:hover {
	background-color: #f8f9fa;
}

.reactions-list {
	max-height: 24rem;
	overflow-y: auto;
}

.icon-sm {
	width: 1rem;
	height: 1rem;
}

.icon-md {
	width: 1.25rem;
	height: 1.25rem;
}

.text-red-500 {
	color: #ef4444 !important;
}

.text-blue-500 {
	color: #3b82f6 !important;
}

.text-yellow-500 {
	color: #eab308 !important;
}

.badge-count {
	font-size: 0.75rem;
	padding: 0.125rem 0.5rem;
}

/* Bootstrap-like utilities */
.card {
	border: 1px solid rgba(0, 0, 0, 0.125);
	border-radius: 0.375rem;
	background-color: #fff;
}

.shadow {
	box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}

.card-header {
	padding: 0.75rem 1.25rem;
	margin-bottom: 0;
	background-color: rgba(0, 0, 0, 0.03);
	border-bottom: 1px solid rgba(0, 0, 0, 0.125);
}

.border-bottom {
	border-bottom: 1px solid #dee2e6;
}

.d-flex {
	display: flex;
}

.justify-content-between {
	justify-content: space-between;
}

.align-items-center {
	align-items: center;
}

.gap-2 {
	gap: 0.5rem;
}

.gap-3 {
	gap: 1rem;
}

.mb-0 {
	margin-bottom: 0;
}

.text-dark {
	color: #212529 !important;
}

.text-muted {
	color: #6c757d !important;
}

.p-3 {
	padding: 1rem;
}

.p-5 {
	padding: 3rem;
}

.text-center {
	text-align: center;
}

.rounded-circle {
	border-radius: 50%;
}

.flex-grow-1 {
	flex-grow: 1;
}

.small {
	font-size: 0.875em;
}

.ms-2 {
	margin-left: 0.5rem;
}

.badge {
	display: inline-block;
	padding: 0.35em 0.65em;
	font-size: 0.75em;
	font-weight: 700;
	line-height: 1;
	color: #fff;
	text-align: center;
	white-space: nowrap;
	vertical-align: baseline;
	border-radius: 0.375rem;
}

.bg-secondary {
	background-color: #6c757d;
}
</style>
