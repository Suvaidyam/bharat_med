<template>
	<div class="min-h-screen bg-gray-50 p-4 md:p-6">
		<!-- Header -->
		<div class="mb-8">
			<h1 class="text-3xl font-bold text-gray-900 mb-2">Reports</h1>
			<p class="text-gray-600">Access and generate detailed reports for your clinic</p>
		</div>

		<!-- Reports Grid -->
		<div class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
			<!-- Appointment Reports -->
			<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
				<div class="flex items-start mb-4">
					<div class="flex-shrink-0 mr-3">
						<div
							class="w-8 h-8 bg-gray-100 rounded-lg flex items-center justify-center"
						>
							<svg
								class="w-5 h-5 text-gray-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M8 7V3a1 1 0 011-1h6a1 1 0 011 1v4m-6 0h6m-6 0V5a1 1 0 00-1 1v1m7-1a1 1 0 00-1-1V5a1 1 0 00-1-1m6 0v16a2 2 0 01-2 2H4a2 2 0 01-2-2V7a2 2 0 012-2h16a2 2 0 012 2z"
								/>
							</svg>
						</div>
					</div>
					<div class="flex-1">
						<h3 class="text-lg font-semibold text-gray-900 mb-1">
							Appointment Reports
						</h3>
						<p class="text-sm text-gray-500">
							Track appointment metrics, trends, and patient attendance
						</p>
					</div>
				</div>

				<div class="space-y-3 mb-6">
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Total Appointments</span>
						<span class="text-sm font-medium text-gray-900">{{
							appointmentReports.totalAppointments.toLocaleString()
						}}</span>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Completion Rate</span>
						<span class="text-sm font-medium text-gray-900"
							>{{ appointmentReports.completionRate }}%</span
						>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">No-Show Rate</span>
						<span class="text-sm font-medium text-gray-900"
							>{{ appointmentReports.noShowRate }}%</span
						>
					</div>
				</div>

				<button
					class="w-full bg-gray-900 text-white py-2.5 px-4 rounded-md text-sm font-medium hover:bg-gray-800 transition-colors"
				>
					View Report
				</button>
			</div>

			<!-- Financial Reports -->
			<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
				<div class="flex items-start mb-4">
					<div class="flex-shrink-0 mr-3">
						<div
							class="w-8 h-8 bg-gray-100 rounded-lg flex items-center justify-center"
						>
							<svg
								class="w-5 h-5 text-gray-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
								/>
							</svg>
						</div>
					</div>
					<div class="flex-1">
						<h3 class="text-lg font-semibold text-gray-900 mb-1">Financial Reports</h3>
						<p class="text-sm text-gray-500">
							Track revenue, expenses, and financial performance
						</p>
					</div>
				</div>

				<div class="space-y-3 mb-6">
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Total Revenue</span>
						<span class="text-sm font-medium text-gray-900"
							>${{ financialReports.totalRevenue.toLocaleString() }}</span
						>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Net Profit</span>
						<span class="text-sm font-medium text-gray-900"
							>${{ financialReports.netProfit.toLocaleString() }}</span
						>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Growth</span>
						<span class="text-sm font-medium text-green-600"
							>+{{ financialReports.growth }}%</span
						>
					</div>
				</div>

				<button
					class="w-full bg-gray-900 text-white py-2.5 px-4 rounded-md text-sm font-medium hover:bg-gray-800 transition-colors"
				>
					View Report
				</button>
			</div>

			<!-- Patient Visit Reports -->
			<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
				<div class="flex items-start mb-4">
					<div class="flex-shrink-0 mr-3">
						<div
							class="w-8 h-8 bg-gray-100 rounded-lg flex items-center justify-center"
						>
							<svg
								class="w-5 h-5 text-gray-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
								/>
							</svg>
						</div>
					</div>
					<div class="flex-1">
						<h3 class="text-lg font-semibold text-gray-900 mb-1">
							Patient Visit Reports
						</h3>
						<p class="text-sm text-gray-500">
							Analyze patient visits, demographics, and health trends
						</p>
					</div>
				</div>

				<div class="space-y-3 mb-6">
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Total Visits</span>
						<span class="text-sm font-medium text-gray-900">{{
							patientVisitReports.totalVisits.toLocaleString()
						}}</span>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">New Patients</span>
						<span class="text-sm font-medium text-gray-900">{{
							patientVisitReports.newPatients
						}}</span>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Avg. Duration</span>
						<span class="text-sm font-medium text-gray-900"
							>{{ patientVisitReports.avgDuration }} min</span
						>
					</div>
				</div>

				<button
					class="w-full bg-gray-900 text-white py-2.5 px-4 rounded-md text-sm font-medium hover:bg-gray-800 transition-colors"
				>
					View Report
				</button>
			</div>

			<!-- Inventory Reports -->
			<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
				<div class="flex items-start mb-4">
					<div class="flex-shrink-0 mr-3">
						<div
							class="w-8 h-8 bg-gray-100 rounded-lg flex items-center justify-center"
						>
							<svg
								class="w-5 h-5 text-gray-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"
								/>
							</svg>
						</div>
					</div>
					<div class="flex-1">
						<h3 class="text-lg font-semibold text-gray-900 mb-1">Inventory Reports</h3>
						<p class="text-sm text-gray-500">
							Track inventory levels, usage, and supply chain metrics
						</p>
					</div>
				</div>

				<div class="space-y-3 mb-6">
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Total Items</span>
						<span class="text-sm font-medium text-gray-900">{{
							inventoryReports.totalItems.toLocaleString()
						}}</span>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Low Stock</span>
						<span class="text-sm font-medium text-red-600">{{
							inventoryReports.lowStock
						}}</span>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Inventory Value</span>
						<span class="text-sm font-medium text-gray-900"
							>${{ inventoryReports.inventoryValue.toLocaleString() }}</span
						>
					</div>
				</div>

				<button
					class="w-full bg-gray-900 text-white py-2.5 px-4 rounded-md text-sm font-medium hover:bg-gray-800 transition-colors"
				>
					View Report
				</button>
			</div>

			<!-- Staff Performance -->
			<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
				<div class="flex items-start mb-4">
					<div class="flex-shrink-0 mr-3">
						<div
							class="w-8 h-8 bg-gray-100 rounded-lg flex items-center justify-center"
						>
							<svg
								class="w-5 h-5 text-gray-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
								/>
							</svg>
						</div>
					</div>
					<div class="flex-1">
						<h3 class="text-lg font-semibold text-gray-900 mb-1">Staff Performance</h3>
						<p class="text-sm text-gray-500">
							Evaluate staff productivity, attendance, and performance
						</p>
					</div>
				</div>

				<div class="space-y-3 mb-6">
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Staff Count</span>
						<span class="text-sm font-medium text-gray-900">{{
							staffPerformance.staffCount
						}}</span>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Avg. Attendance</span>
						<span class="text-sm font-medium text-gray-900"
							>{{ staffPerformance.avgAttendance }}%</span
						>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Productivity</span>
						<span class="text-sm font-medium text-gray-900"
							>{{ staffPerformance.productivity }}%</span
						>
					</div>
				</div>

				<div
					class="w-full bg-gray-100 text-gray-500 py-2.5 px-4 rounded-md text-sm font-medium text-center"
				>
					Coming Soon
				</div>
			</div>

			<!-- Custom Reports -->
			<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
				<div class="flex items-start mb-4">
					<div class="flex-shrink-0 mr-3">
						<div
							class="w-8 h-8 bg-gray-100 rounded-lg flex items-center justify-center"
						>
							<svg
								class="w-5 h-5 text-gray-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 100 4m0-4v2m0-6V4"
								/>
							</svg>
						</div>
					</div>
					<div class="flex-1">
						<h3 class="text-lg font-semibold text-gray-900 mb-1">Custom Reports</h3>
						<p class="text-sm text-gray-500">
							Create customized reports with specific metrics and filters
						</p>
					</div>
				</div>

				<div class="space-y-3 mb-6">
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Saved Reports</span>
						<span class="text-sm font-medium text-gray-900">{{
							customReports.savedReports
						}}</span>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Templates</span>
						<span class="text-sm font-medium text-gray-900">{{
							customReports.templates
						}}</span>
					</div>
					<div class="flex justify-between">
						<span class="text-sm text-gray-600">Export Options</span>
						<span class="text-sm font-medium text-gray-900">{{
							customReports.exportOptions
						}}</span>
					</div>
				</div>

				<div
					class="w-full bg-gray-100 text-gray-500 py-2.5 px-4 rounded-md text-sm font-medium text-center"
				>
					Coming Soon
				</div>
			</div>
		</div>

		<!-- Quick Actions -->
		<div class="mt-8 bg-white rounded-lg shadow-sm border border-gray-200 p-6">
			<h3 class="text-lg font-semibold text-gray-900 mb-4">Quick Actions</h3>
			<div class="flex flex-wrap gap-3">
				<button
					v-for="action in quickActions"
					:key="action.id"
					:class="[
						'px-4 py-2 rounded-md text-sm font-medium transition-colors',
						action.primary
							? 'bg-blue-600 text-white hover:bg-blue-700'
							: 'bg-gray-100 text-gray-700 hover:bg-gray-200',
					]"
				>
					{{ action.label }}
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'

// Report data
const appointmentReports = ref({
	totalAppointments: 1248,
	completionRate: 70.2,
	noShowRate: 6.6,
})

const financialReports = ref({
	totalRevenue: 128450,
	netProfit: 41125,
	growth: 12.8,
})

const patientVisitReports = ref({
	totalVisits: 3642,
	newPatients: 428,
	avgDuration: 32,
})

const inventoryReports = ref({
	totalItems: 1245,
	lowStock: 32,
	inventoryValue: 248320,
})

const staffPerformance = ref({
	staffCount: 48,
	avgAttendance: 92.5,
	productivity: 87.3,
})

const customReports = ref({
	savedReports: 5,
	templates: 12,
	exportOptions: 'PDF, CSV, Excel',
})

// Quick actions
const quickActions = ref([
	{ id: 1, label: 'Generate Monthly Report', primary: true },
	{ id: 2, label: 'Export Data', primary: false },
	{ id: 3, label: 'Schedule Report', primary: false },
	{ id: 4, label: 'Compare Periods', primary: false },
	{ id: 5, label: 'Create Custom Report', primary: false },
])
</script>
