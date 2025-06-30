<template>
	<div class="min-h-screen">
		<!-- Header -->
		<div class="bg-white px-4 py-4 sm:px-6">
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
				<div class="flex items-center gap-2">
					<span class="text-gray-500">Ambulances /</span>
					<span class="font-semibold text-gray-900">AMB-002</span>
					<span
						class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800"
					>
						Available
					</span>
				</div>
				<div class="flex flex-col sm:flex-row gap-2">
					<button
						class="inline-flex items-center px-3 py-2 border border-gray-300 shadow-sm text-sm leading-4 font-medium rounded-sm text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
					>
						<svg
							class="mr-2 h-4 w-4"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
							/>
						</svg>
						Schedule Maintenance
					</button>
					<button
						class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-sm text-white bg-gray-800 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
					>
						<svg
							class="mr-2 h-4 w-4"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
							/>
						</svg>
						Update Status
					</button>
				</div>
			</div>
		</div>

		<!-- Status Cards -->
		<div class="px-4 py-6 sm:px-6">
			<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
				<!-- Status Card -->
				<div class="bg-white overflow-hidden shadow rounded-sm">
					<div class="p-5">
						<div class="flex items-center">
							<div class="flex-shrink-0">
								<svg
									class="h-6 w-6 text-gray-400"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
									/>
								</svg>
							</div>
							<div class="ml-5 w-0 flex-1">
								<dl>
									<dt class="text-sm font-medium text-gray-500 truncate">
										Status
									</dt>
									<dd class="text-lg font-medium text-gray-900">Available</dd>
									<dd class="text-xs text-gray-500">
										Last updated: Today, 9:30 AM
									</dd>
								</dl>
							</div>
						</div>
					</div>
				</div>

				<!-- Last Maintenance Card -->
				<div class="bg-white overflow-hidden shadow rounded-sm">
					<div class="p-5">
						<div class="flex items-center">
							<div class="flex-shrink-0">
								<svg
									class="h-6 w-6 text-gray-400"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
									/>
								</svg>
							</div>
							<div class="ml-5 w-0 flex-1">
								<dl>
									<dt class="text-sm font-medium text-gray-500 truncate">
										Last Maintenance
									</dt>
									<dd class="text-lg font-medium text-gray-900">2023-04-02</dd>
									<dd class="text-xs text-gray-500">Next: 2023-07-02</dd>
								</dl>
							</div>
						</div>
					</div>
				</div>

				<!-- Total Calls Card -->
				<div class="bg-white overflow-hidden shadow rounded-sm">
					<div class="p-5">
						<div class="flex items-center">
							<div class="flex-shrink-0">
								<svg
									class="h-6 w-6 text-gray-400"
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
							<div class="ml-5 w-0 flex-1">
								<dl>
									<dt class="text-sm font-medium text-gray-500 truncate">
										Total Calls
									</dt>
									<dd class="text-lg font-medium text-gray-900">42</dd>
									<dd class="text-xs text-gray-500">5 calls this month</dd>
								</dl>
							</div>
						</div>
					</div>
				</div>

				<!-- Current Driver Card -->
				<div class="bg-white overflow-hidden shadow rounded-sm">
					<div class="p-5">
						<div class="flex items-center">
							<div class="flex-shrink-0">
								<svg
									class="h-6 w-6 text-gray-400"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
									/>
								</svg>
							</div>
							<div class="ml-5 w-0 flex-1">
								<dl>
									<dt class="text-sm font-medium text-gray-500 truncate">
										Current Driver
									</dt>
									<dd class="text-lg font-medium text-gray-900">Sarah Wilson</dd>
									<dd class="text-xs text-gray-500">
										Assigned since April 1, 2023
									</dd>
								</dl>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Navigation Tabs -->
		<div class="px-4 sm:px-6">
			<div class="border-b border-gray-200">
				<nav class="-mb-px flex space-x-8">
					<button
						v-for="tab in tabs"
						:key="tab.name"
						@click="activeTab = tab.name"
						:class="[
							activeTab === tab.name
								? 'border-indigo-500 text-indigo-600'
								: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
							'whitespace-nowrap py-2 px-1 border-b-2 font-medium text-sm',
						]"
					>
						{{ tab.label }}
					</button>
				</nav>
			</div>
		</div>

		<!-- Content Area -->
		<div class="px-4 py-6 sm:px-6">
			<div v-if="activeTab === 'overview'">
				<!-- Ambulance Overview -->
				<div class="bg-white shadow overflow-hidden sm:rounded-sm mb-6">
					<div class="px-4 py-5 sm:px-6">
						<h3 class="text-lg leading-6 font-medium text-gray-900">
							Ambulance Overview
						</h3>
						<p class="mt-1 max-w-2xl text-sm text-gray-500">
							General information and specifications
						</p>
					</div>
					<div class="border-t border-gray-200">
						<div class="grid grid-cols-1 lg:grid-cols-2 gap-0">
							<!-- General Information -->
							<div class="px-4 py-5 sm:px-6">
								<h4 class="text-base font-medium text-gray-900 mb-4">
									General Information
								</h4>
								<dl class="space-y-3">
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">ID:</dt>
										<dd class="text-gray-900">AMB-002</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Registration:</dt>
										<dd class="text-gray-900">ABC-5678</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Model:</dt>
										<dd class="text-gray-900">Mercedes Sprinter</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Year:</dt>
										<dd class="text-gray-900">2022</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Type:</dt>
										<dd class="text-gray-900">Advanced Life Support</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Purchase Date:</dt>
										<dd class="text-gray-900">2022-01-15</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Insurance Expiry:</dt>
										<dd class="text-gray-900">2024-01-15</dd>
									</div>
								</dl>
							</div>

							<!-- Technical Specifications -->
							<div
								class="px-4 py-5 sm:px-6 border-t lg:border-t-0 lg:border-l border-gray-200"
							>
								<h4 class="text-base font-medium text-gray-900 mb-4">
									Technical Specifications
								</h4>
								<dl class="space-y-3">
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Fuel Type:</dt>
										<dd class="text-gray-900">Diesel</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Mileage:</dt>
										<dd class="text-gray-900">12,450 km</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Capacity:</dt>
										<dd class="text-gray-900">2 stretchers, 3 seated</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Current Location:</dt>
										<dd class="text-gray-900">East Wing</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Current Driver:</dt>
										<dd class="text-gray-900">Sarah Wilson</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Last Maintenance:</dt>
										<dd class="text-gray-900">2023-04-02</dd>
									</div>
									<div class="flex justify-between text-sm">
										<dt class="text-gray-500">Next Maintenance:</dt>
										<dd class="text-gray-900">2023-07-02</dd>
									</div>
								</dl>
							</div>
						</div>
					</div>
				</div>

				<!-- Usage Statistics -->
				<div class="bg-white shadow overflow-hidden sm:rounded-sm">
					<div class="px-4 py-5 sm:px-6">
						<h3 class="text-lg leading-6 font-medium text-gray-900">
							Usage Statistics
						</h3>
					</div>
					<div class="border-t border-gray-200">
						<div class="grid grid-cols-1 md:grid-cols-3 gap-0">
							<!-- Total Distance -->
							<div
								class="px-4 py-5 sm:px-6 text-center border-b md:border-b-0 md:border-r border-gray-200"
							>
								<div class="flex items-center justify-center mb-2">
									<svg
										class="h-5 w-5 text-gray-400 mr-2"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
										/>
									</svg>
									<h4 class="text-sm font-medium text-gray-900">
										Total Distance
									</h4>
								</div>
								<p class="text-2xl font-bold text-gray-900">12,450 km</p>
								<p class="text-xs text-gray-500">+450 km this month</p>
							</div>

							<!-- Average Response Time -->
							<div
								class="px-4 py-5 sm:px-6 text-center border-b md:border-b-0 md:border-r border-gray-200"
							>
								<div class="flex items-center justify-center mb-2">
									<svg
										class="h-5 w-5 text-gray-400 mr-2"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
										/>
									</svg>
									<h4 class="text-sm font-medium text-gray-900">
										Average Response Time
									</h4>
								</div>
								<p class="text-2xl font-bold text-gray-900">8.2 min</p>
								<p class="text-xs text-gray-500">-0.5 min from last month</p>
							</div>

							<!-- Fuel Efficiency -->
							<div class="px-4 py-5 sm:px-6 text-center">
								<div class="flex items-center justify-center mb-2">
									<svg
										class="h-5 w-5 text-gray-400 mr-2"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
										/>
									</svg>
									<h4 class="text-sm font-medium text-gray-900">
										Fuel Efficiency
									</h4>
								</div>
								<p class="text-2xl font-bold text-gray-900">9.8 L/100km</p>
								<p class="text-xs text-gray-500">Within normal range</p>
							</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Other tab content would go here -->
			<div v-else class="bg-white shadow overflow-hidden sm:rounded-sm">
				<div class="px-4 py-5 sm:px-6">
					<h3 class="text-lg leading-6 font-medium text-gray-900">
						{{ activeTab.charAt(0).toUpperCase() + activeTab.slice(1) }}
					</h3>
					<p class="mt-1 max-w-2xl text-sm text-gray-500">
						Content for {{ activeTab }} tab
					</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('overview')

const tabs = [
	{ name: 'overview', label: 'Overview' },
	{ name: 'maintenance', label: 'Maintenance' },
	{ name: 'equipment', label: 'Equipment' },
	{ name: 'assignments', label: 'Call Assignments' },
]
</script>
