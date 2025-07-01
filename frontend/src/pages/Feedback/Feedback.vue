<template>
	<div class="min-h-screen bg-gray-50 p-4 md:p-6">
		<!-- Header -->
		<div class="mb-8">
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
				<div>
					<h1 class="text-2xl font-bold text-gray-900">Feedback Management</h1>
					<p class="text-sm text-gray-500 mt-1">
						Create and manage patient feedback surveys
					</p>
				</div>
				<div class="flex items-center gap-3">
					<button
						class="flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
					>
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 10v6m0 0l-3-3m3 3l3-3M3 17V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2z"
							/>
						</svg>
						Export
					</button>
					<button
						class="px-4 py-2 text-sm font-medium text-white bg-gray-800 rounded-md hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-500"
					>
						Create Survey
					</button>
				</div>
			</div>
		</div>

		<!-- Stats Cards -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
			<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
				<div class="text-sm font-medium text-gray-500 mb-2">Total Surveys</div>
				<div class="text-3xl font-bold text-gray-900">{{ stats.totalSurveys }}</div>
				<div class="text-xs text-gray-400 mt-1">5 active surveys</div>
			</div>

			<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
				<div class="text-sm font-medium text-gray-500 mb-2">Total Responses</div>
				<div class="text-3xl font-bold text-gray-900">{{ stats.totalResponses }}</div>
				<div class="text-xs text-gray-400 mt-1">330 responses</div>
			</div>

			<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
				<div class="text-sm font-medium text-gray-500 mb-2">Average Rating</div>
				<div class="text-3xl font-bold text-gray-900">{{ stats.averageRating }}/5</div>
				<div class="text-xs text-gray-400 mt-1">Overall satisfaction</div>
			</div>

			<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
				<div class="text-sm font-medium text-gray-500 mb-2">Completion Rate</div>
				<div class="text-3xl font-bold text-gray-900">{{ stats.completionRate }}%</div>
				<div class="text-xs text-gray-400 mt-1">74% completion percentage</div>
			</div>
		</div>

		<!-- Navigation Tabs -->
		<div class="mb-6">
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
				<div class="flex space-x-8 border-b border-gray-200">
					<button
						v-for="tab in tabs"
						:key="tab.id"
						@click="activeTab = tab.id"
						:class="[
							'py-2 px-1 border-b-2 font-medium text-sm transition-colors',
							activeTab === tab.id
								? 'border-blue-500 text-blue-600'
								: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
						]"
					>
						{{ tab.name }}
					</button>
				</div>

				<div class="flex items-center gap-4">
					<div class="relative">
						<input
							v-model="searchQuery"
							type="text"
							placeholder="Search surveys..."
							class="w-full sm:w-64 pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
						/>
						<svg
							class="absolute left-3 top-2.5 h-4 w-4 text-gray-400"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
							/>
						</svg>
					</div>

					<select
						v-model="statusFilter"
						class="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
					>
						<option value="all">All Status</option>
						<option value="active">Active</option>
						<option value="draft">Draft</option>
					</select>
				</div>
			</div>

			<div class="text-sm text-gray-500 mt-4">
				Showing {{ filteredSurveys.length }} of {{ surveys.length }} surveys
			</div>
		</div>

		<!-- Survey Cards -->
		<div class="space-y-4">
			<div
				v-for="survey in filteredSurveys"
				:key="survey.id"
				class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow"
			>
				<div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
					<div class="flex-1">
						<div class="flex items-start justify-between mb-3">
							<div>
								<h3 class="text-lg font-semibold text-gray-900 mb-1">
									{{ survey.title }}
								</h3>
								<p class="text-sm text-gray-500">{{ survey.description }}</p>
							</div>
							<button class="text-gray-400 hover:text-gray-600">
								<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
									<path
										d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
									/>
								</svg>
							</button>
						</div>

						<div class="flex flex-wrap items-center gap-4 text-sm">
							<div class="flex items-center gap-2">
								<span class="text-gray-500">Status</span>
								<span
									:class="[
										'px-2 py-1 rounded-full text-xs font-medium',
										survey.status === 'active'
											? 'bg-green-100 text-green-800'
											: 'bg-gray-100 text-gray-800',
									]"
								>
									{{ survey.status }}
								</span>
							</div>

							<div class="flex items-center gap-2">
								<span class="text-gray-500">Responses</span>
								<span class="font-medium text-gray-900">{{
									survey.responses
								}}</span>
							</div>

							<div class="flex items-center gap-2">
								<span class="text-gray-500">Average Rating</span>
								<span class="font-medium text-gray-900">
									{{ survey.averageRating || 'N/A' }}
									<span v-if="survey.averageRating" class="text-gray-400">{{
										survey.ratingTrend
									}}</span>
								</span>
							</div>
						</div>
					</div>

					<div class="flex flex-col items-end gap-2">
						<!-- Progress Bar -->
						<div class="w-full lg:w-48">
							<div class="flex justify-between text-xs text-gray-500 mb-1">
								<span>Completion Rate</span>
								<span>{{ survey.completionRate }}%</span>
							</div>
							<div class="w-full bg-gray-200 rounded-full h-2">
								<div
									class="bg-blue-500 h-2 rounded-full transition-all duration-300"
									:style="{ width: survey.completionRate + '%' }"
								></div>
							</div>
						</div>

						<div class="text-xs text-gray-400">
							Created on {{ formatDate(survey.createdDate) }} • Last updated
							{{ formatDate(survey.updatedDate) }}
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Empty State -->
		<div v-if="filteredSurveys.length === 0" class="text-center py-12">
			<div class="text-gray-500 mb-4">
				<svg
					class="mx-auto h-12 w-12"
					fill="none"
					stroke="currentColor"
					viewBox="0 0 24 24"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
					/>
				</svg>
			</div>
			<h3 class="text-lg font-medium text-gray-900 mb-2">No surveys found</h3>
			<p class="text-gray-500">Try adjusting your search or filter criteria.</p>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const activeTab = ref('surveys')
const searchQuery = ref('')
const statusFilter = ref('all')

// Stats data
const stats = ref({
	totalSurveys: 5,
	totalResponses: 330,
	averageRating: 4.1,
	completionRate: 74,
})

// Navigation tabs
const tabs = ref([
	{ id: 'surveys', name: 'Surveys' },
	{ id: 'responses', name: 'Recent Responses' },
	{ id: 'analytics', name: 'Analytics' },
])

// Survey data
const surveys = ref([
	{
		id: 1,
		title: 'Patient Satisfaction Survey',
		description: 'General satisfaction survey for all patients',
		status: 'active',
		responses: 128,
		averageRating: 4.2,
		ratingTrend: '↑',
		completionRate: 78,
		createdDate: new Date('2023-10-15'),
		updatedDate: new Date('2023-10-14'),
	},
	{
		id: 2,
		title: 'Emergency Department Experience',
		description: 'Feedback on emergency department visits',
		status: 'active',
		responses: 64,
		averageRating: 3.8,
		ratingTrend: '↓',
		completionRate: 65,
		createdDate: new Date('2023-10-20'),
		updatedDate: new Date('2023-10-14'),
	},
	{
		id: 3,
		title: 'Outpatient Services Feedback',
		description: 'Survey for outpatient department services',
		status: 'draft',
		responses: 0,
		averageRating: null,
		ratingTrend: '',
		completionRate: 0,
		createdDate: new Date('2023-10-14'),
		updatedDate: new Date('2023-10-14'),
	},
	{
		id: 4,
		title: 'Telemedicine Consultation Feedback',
		description: 'Feedback on virtual consultations',
		status: 'active',
		responses: 42,
		averageRating: 4.5,
		ratingTrend: '↑',
		completionRate: 82,
		createdDate: new Date('2023-10-13'),
		updatedDate: new Date('2023-10-14'),
	},
])

// Computed properties
const filteredSurveys = computed(() => {
	return surveys.value.filter((survey) => {
		const matchesSearch =
			survey.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			survey.description.toLowerCase().includes(searchQuery.value.toLowerCase())

		const matchesStatus = statusFilter.value === 'all' || survey.status === statusFilter.value

		return matchesSearch && matchesStatus
	})
})

// Methods
const formatDate = (date) => {
	return date.toLocaleDateString('en-US', {
		month: '2-digit',
		day: '2-digit',
		year: 'numeric',
	})
}
</script>
